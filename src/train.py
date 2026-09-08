"""
Run with:  python -m src.train

Loads data/raw -> cleans -> engineers features -> generates risk labels ->
splits -> trains baseline ML models + deep learning model -> evaluates ->
saves all artifacts to models/ and outputs/.

Will raise a clear error (not fabricate data) if data/raw/ is empty.
"""
from __future__ import annotations

import json
import logging

import joblib
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from . import config, data_cleaning, data_loader, evaluate, feature_engineering, risk_scoring, utils

logger = logging.getLogger(__name__)

FEATURE_COLUMNS = [
    "crime_rate", "crime_rate_prev_year", "crime_rate_yoy_change",
    "crime_rate_yoy_pct_change", "crime_rate_rolling_mean", "crime_rate_trend_slope",
    "rape_cases_share", "kidnapping_abduction_cases_share", "dowry_death_cases_share",
    "assault_on_modesty_cases_share", "cruelty_498a_cases_share",
]


def prepare_dataset() -> pd.DataFrame:
    raw = data_loader.load_and_combine()
    cleaned, quality_report = data_cleaning.clean(raw)
    quality_report.save(config.REPORTS_DIR / "data_quality_report.json")
    logger.info("Data quality report saved.")

    featured = feature_engineering.build_features(cleaned)
    labeled = risk_scoring.compute_labels(featured)
    labeled = labeled.dropna(subset=["risk_label"]).reset_index(drop=True)

    if labeled.empty:
        raise data_loader.DatasetNotFoundError(
            "After cleaning and labeling, no usable rows remained. This usually "
            "means the placed dataset lacks enough historical rows per city to "
            "compute a trend, or crime_rate could not be derived. Check "
            "data/dataset_sources.md and consider a dataset with more years of "
            "coverage per city."
        )
    return labeled


def split_features(df: pd.DataFrame):
    available_features = [c for c in FEATURE_COLUMNS if c in df.columns]
    if not available_features:
        raise ValueError("No configured feature columns are present after feature engineering.")

    X = df[available_features].copy()
    y_raw = df["risk_label"].copy()

    imputer = SimpleImputer(strategy="median")
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=available_features, index=X.index)

    label_encoder = LabelEncoder()
    label_encoder.fit(list(config.RISK_CONFIG.class_labels))
    y = label_encoder.transform(y_raw)

    return X_imputed, y, available_features, imputer, label_encoder


def train_baselines(X_train, y_train, X_val, y_val, class_weight):
    models = {
        "logistic_regression": LogisticRegression(max_iter=1000, class_weight=class_weight),
        "decision_tree": DecisionTreeClassifier(random_state=config.RANDOM_SEED, class_weight=class_weight),
        "random_forest": RandomForestClassifier(
            n_estimators=300, random_state=config.RANDOM_SEED, class_weight=class_weight
        ),
    }
    fitted = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        fitted[name] = model
        logger.info("Trained baseline model: %s", name)
    return fitted


def build_dl_model(input_dim: int, n_classes: int):
    import tensorflow as tf
    from tensorflow.keras import layers, models

    cfg = config.TRAIN_CONFIG
    inputs = layers.Input(shape=(input_dim,))
    x = inputs
    for units in cfg.dl_hidden_units:
        x = layers.Dense(units, activation="relu")(x)
        x = layers.BatchNormalization()(x)
        x = layers.Dropout(cfg.dl_dropout)(x)
    outputs = layers.Dense(n_classes, activation="softmax")(x)

    model = models.Model(inputs, outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model


def train_dl(X_train, y_train, X_val, y_val, n_classes, class_weight=None):
    import tensorflow as tf

    cfg = config.TRAIN_CONFIG
    model = build_dl_model(X_train.shape[1], n_classes)

    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss", patience=cfg.dl_patience, restore_best_weights=True
        ),
        tf.keras.callbacks.ModelCheckpoint(
            str(config.MODELS_DIR / "deep_learning_model.keras"),
            monitor="val_loss", save_best_only=True,
        ),
        tf.keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=5),
    ]

    class_weight_dict = None
    if class_weight is not None:
        classes, counts = np.unique(y_train, return_counts=True)
        total = counts.sum()
        class_weight_dict = {int(c): total / (len(classes) * cnt) for c, cnt in zip(classes, counts)}

    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=cfg.dl_epochs,
        batch_size=cfg.dl_batch_size,
        callbacks=callbacks,
        class_weight=class_weight_dict,
        verbose=2,
    )
    return model, history


def main():
    utils.configure_logging()
    utils.set_seed(config.RANDOM_SEED)

    logger.info("Loading and preparing dataset...")
    df = prepare_dataset()
    df.to_parquet(config.PROCESSED_DIR / "featured_labeled_dataset.parquet", index=False)

    X, y, feature_names, imputer, label_encoder = split_features(df)
    cfg = config.TRAIN_CONFIG

    X_trainval, X_test, y_trainval, y_test = train_test_split(
        X, y, test_size=cfg.test_size, random_state=cfg.random_seed, stratify=y
    )
    val_fraction_of_trainval = cfg.val_size / (1 - cfg.test_size)
    X_train, X_val, y_train, y_val = train_test_split(
        X_trainval, y_trainval, test_size=val_fraction_of_trainval,
        random_state=cfg.random_seed, stratify=y_trainval,
    )

    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_val_s = scaler.transform(X_val)
    X_test_s = scaler.transform(X_test)

    class_weight = "balanced" if cfg.use_class_weights else None

    logger.info("Training baseline models...")
    baselines = train_baselines(X_train_s, y_train, X_val_s, y_val, class_weight)

    logger.info("Training deep learning model...")
    dl_model, history = train_dl(
        X_train_s, y_train, X_val_s, y_val,
        n_classes=len(config.RISK_CONFIG.class_labels),
        class_weight=cfg.use_class_weights,
    )

    logger.info("Evaluating all models on held-out test set...")
    results = evaluate.evaluate_all(
        baselines=baselines, dl_model=dl_model,
        X_test=X_test_s, y_test=y_test,
        label_encoder=label_encoder,
        history=history,
    )

    joblib.dump(scaler, config.MODELS_DIR / "scaler.pkl")
    joblib.dump(imputer, config.MODELS_DIR / "imputer.pkl")
    joblib.dump(label_encoder, config.MODELS_DIR / "label_encoder.pkl")
    joblib.dump(baselines["random_forest"], config.MODELS_DIR / "baseline_model.pkl")
    with open(config.MODELS_DIR / "feature_names.json", "w") as f:
        json.dump(feature_names, f, indent=2)

    logger.info("Training complete. Artifacts saved to %s", config.MODELS_DIR)
    logger.info("Model comparison:\n%s", results.to_string(index=False))


if __name__ == "__main__":
    main()

"""
Run with:  python -m src.predict
Reusable prediction logic, also imported directly by the Streamlit app.
"""
from __future__ import annotations

import json
import logging

import joblib
import numpy as np
import pandas as pd

from . import config

logger = logging.getLogger(__name__)


class ArtifactsNotFoundError(RuntimeError):
    """Raised when models/ doesn't have trained artifacts yet."""


def artifacts_exist() -> bool:
    required = [
        "deep_learning_model.keras", "scaler.pkl", "imputer.pkl",
        "label_encoder.pkl", "feature_names.json",
    ]
    return all((config.MODELS_DIR / f).exists() for f in required)


def load_artifacts():
    if not artifacts_exist():
        raise ArtifactsNotFoundError(
            "No trained model found in models/. Run `python -m src.train` first "
            "(after placing a real dataset in data/raw/ — see data/dataset_sources.md)."
        )
    import tensorflow as tf

    dl_model = tf.keras.models.load_model(config.MODELS_DIR / "deep_learning_model.keras")
    scaler = joblib.load(config.MODELS_DIR / "scaler.pkl")
    imputer = joblib.load(config.MODELS_DIR / "imputer.pkl")
    label_encoder = joblib.load(config.MODELS_DIR / "label_encoder.pkl")
    baseline_model = joblib.load(config.MODELS_DIR / "baseline_model.pkl")
    with open(config.MODELS_DIR / "feature_names.json") as f:
        feature_names = json.load(f)

    return {
        "dl_model": dl_model, "scaler": scaler, "imputer": imputer,
        "label_encoder": label_encoder, "baseline_model": baseline_model,
        "feature_names": feature_names,
    }


def predict_risk(feature_row: dict, artifacts: dict) -> dict:
    """feature_row: dict of {feature_name: value}, missing keys are imputed."""
    feature_names = artifacts["feature_names"]
    X = pd.DataFrame([{f: feature_row.get(f, np.nan) for f in feature_names}])
    X_imputed = artifacts["imputer"].transform(X)
    X_scaled = artifacts["scaler"].transform(X_imputed)

    proba = artifacts["dl_model"].predict(X_scaled, verbose=0)[0]
    pred_idx = int(np.argmax(proba))
    label = artifacts["label_encoder"].inverse_transform([pred_idx])[0]

    contributions = dict(zip(feature_names, X_imputed[0].tolist()))

    return {
        "predicted_risk": label,
        "model_confidence": float(proba[pred_idx]),
        "class_probabilities": dict(zip(artifacts["label_encoder"].classes_, proba.tolist())),
        "input_features_used": contributions,
    }


def main():
    artifacts = load_artifacts()
    print("Loaded artifacts. Feature names expected:", artifacts["feature_names"])
    print("Provide a feature dict to predict_risk() to get a prediction — "
          "see the Streamlit app (app.py) for an interactive example.")


if __name__ == "__main__":
    main()

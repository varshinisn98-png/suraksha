from __future__ import annotations

import logging

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, classification_report, confusion_matrix,
    f1_score, precision_score, recall_score, roc_auc_score,
)

from . import config

logger = logging.getLogger(__name__)


def _metrics_row(name: str, y_true, y_pred, y_proba=None) -> dict:
    row = {
        "model": name,
        "accuracy": accuracy_score(y_true, y_pred),
        "precision_macro": precision_score(y_true, y_pred, average="macro", zero_division=0),
        "recall_macro": recall_score(y_true, y_pred, average="macro", zero_division=0),
        "f1_macro": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "f1_weighted": f1_score(y_true, y_pred, average="weighted", zero_division=0),
    }
    if y_proba is not None:
        try:
            row["roc_auc_ovr"] = roc_auc_score(y_true, y_proba, multi_class="ovr", average="macro")
        except ValueError:
            row["roc_auc_ovr"] = np.nan
    return row


def plot_confusion_matrix(y_true, y_pred, class_names, out_path, title):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(5, 4))
    im = ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(class_names)))
    ax.set_yticks(range(len(class_names)))
    ax.set_xticklabels(class_names)
    ax.set_yticklabels(class_names)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title(title)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i, j], ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black")
    fig.colorbar(im)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def plot_training_curves(history, out_path):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    axes[0].plot(history.history["loss"], label="train")
    axes[0].plot(history.history["val_loss"], label="val")
    axes[0].set_title("Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].legend()

    axes[1].plot(history.history["accuracy"], label="train")
    axes[1].plot(history.history["val_accuracy"], label="val")
    axes[1].set_title("Accuracy")
    axes[1].set_xlabel("Epoch")
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def evaluate_all(baselines: dict, dl_model, X_test, y_test, label_encoder, history=None) -> pd.DataFrame:
    class_names = list(label_encoder.classes_)
    rows = []

    for name, model in baselines.items():
        y_pred = model.predict(X_test)
        y_proba = model.predict_proba(X_test) if hasattr(model, "predict_proba") else None
        rows.append(_metrics_row(name, y_test, y_pred, y_proba))
        plot_confusion_matrix(
            y_test, y_pred, class_names,
            config.FIGURES_DIR / f"confusion_matrix_{name}.png",
            f"Confusion Matrix — {name}",
        )
        report_txt = classification_report(y_test, y_pred, target_names=class_names, zero_division=0)
        (config.REPORTS_DIR / f"classification_report_{name}.txt").write_text(report_txt)

    dl_proba = dl_model.predict(X_test, verbose=0)
    dl_pred = dl_proba.argmax(axis=1)
    rows.append(_metrics_row("deep_learning_model", y_test, dl_pred, dl_proba))
    plot_confusion_matrix(
        y_test, dl_pred, class_names,
        config.FIGURES_DIR / "confusion_matrix_deep_learning_model.png",
        "Confusion Matrix — Deep Learning Model",
    )
    report_txt = classification_report(y_test, dl_pred, target_names=class_names, zero_division=0)
    (config.REPORTS_DIR / "classification_report_deep_learning_model.txt").write_text(report_txt)

    if history is not None:
        plot_training_curves(history, config.FIGURES_DIR / "dl_training_curves.png")

    results = pd.DataFrame(rows)
    results.to_csv(config.REPORTS_DIR / "model_results.csv", index=False)
    logger.info(
        "Note: for imbalanced risk classes, prioritize macro F1 / recall over raw "
        "accuracy — a model can score high accuracy by always predicting the "
        "majority class while missing HIGH-risk cases entirely."
    )
    return results

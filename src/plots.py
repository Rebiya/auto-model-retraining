# =========================================
# File: src/plots.py
# Purpose: Reusable visualization utilities
# =========================================

import os
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import (
    confusion_matrix,
    roc_curve,
    auc,
    precision_recall_curve
)

sns.set(style="whitegrid")


# -------------------------------
# Utility: numeric versioning
# -------------------------------
def _get_next_version(save_dir: str, prefix: str) -> int:
    """
    Finds the next numeric version for a plot file.
    Example: confusion_matrix_0.png, confusion_matrix_1.png
    """
    if not os.path.exists(save_dir):
        return 0

    pattern = re.compile(rf"{prefix}_(\d+)\.png")
    versions = []

    for f in os.listdir(save_dir):
        match = pattern.match(f)
        if match:
            versions.append(int(match.group(1)))

    return max(versions) + 1 if versions else 0


# -------------------------------
# 1️⃣ Confusion Matrix
# -------------------------------
def plot_confusion_matrix(
    y_true,
    y_pred,
    model_name: str,
    labels=("No Churn", "Churn"),
    base_dir="figures"
):
    save_dir = os.path.join(base_dir, model_name)
    os.makedirs(save_dir, exist_ok=True)

    cm = confusion_matrix(y_true, y_pred)

    version = _get_next_version(save_dir, "confusion_matrix")
    save_path = os.path.join(save_dir, f"confusion_matrix_{version}.png")

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=labels,
        yticklabels=labels
    )
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title(f"{model_name} – Confusion Matrix")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


# -------------------------------
# 2️⃣ ROC Curve + AUC
# -------------------------------
def plot_roc_curve(
    y_true,
    y_proba,
    model_name: str,
    base_dir="figures"
):
    save_dir = os.path.join(base_dir, model_name)
    os.makedirs(save_dir, exist_ok=True)

    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)

    version = _get_next_version(save_dir, "roc_curve")
    save_path = os.path.join(save_dir, f"roc_curve_{version}.png")

    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.4f}")
    plt.plot([0, 1], [0, 1], linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"{model_name} – ROC Curve")
    plt.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


# -------------------------------
# 3️⃣ Precision–Recall Curve
# -------------------------------
def plot_precision_recall_curve(
    y_true,
    y_proba,
    model_name: str,
    base_dir="figures"
):
    save_dir = os.path.join(base_dir, model_name)
    os.makedirs(save_dir, exist_ok=True)

    precision, recall, _ = precision_recall_curve(y_true, y_proba)

    version = _get_next_version(save_dir, "precision_recall_curve")
    save_path = os.path.join(save_dir, f"precision_recall_curve_{version}.png")

    plt.figure(figsize=(6, 5))
    plt.plot(recall, precision)
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(f"{model_name} – Precision-Recall Curve")

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

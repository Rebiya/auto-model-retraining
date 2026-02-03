# =========================================
# File: src/evaluate.py
# Purpose: Compute evaluation metrics and save to results.csv
# =========================================

import os
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)
import numpy as np

RESULTS_FILE = "results.csv"  # root folder


def evaluate_model(
    y_true,
    y_pred,
    y_proba=None,
    model_name="model",
    train_accuracy=None,
    loss=None
):
    """
    Compute metrics and append to results.csv

    Parameters
    ----------
    y_true : array-like
        True labels
    y_pred : array-like
        Predicted labels
    y_proba : array-like, optional
        Predicted probabilities (for ROC AUC)
    model_name : str
        Name of the model
    train_accuracy : float, optional
        Training set accuracy (if available)
    loss : float, optional
        Training loss (if available)

    Returns
    -------
    metrics_dict : dict
        Dictionary of computed metrics
    """

    # Basic metrics
    test_accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    # ROC AUC
    if y_proba is not None:
        try:
            roc_auc = roc_auc_score(y_true, y_proba)
        except ValueError:
            roc_auc = np.nan
    else:
        roc_auc = np.nan

    # Confusion Matrix as string
    cm = confusion_matrix(y_true, y_pred)
    cm_str = np.array2string(cm, separator=",")

    metrics_dict = {
        "model": model_name,
        "train_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "loss": loss,
        "precision_score": precision,
        "recall_score": recall,
        "f1_score": f1,
        "roc_auc_score": roc_auc,
        "confusion_matrix": cm_str
    }

    # Save to results.csv
    if os.path.exists(RESULTS_FILE) and os.path.getsize(RESULTS_FILE) > 0:
        df = pd.read_csv(RESULTS_FILE)
        df = pd.concat([df, pd.DataFrame([metrics_dict])], ignore_index=True)
    else:
        df = pd.DataFrame([metrics_dict])

    df.to_csv(RESULTS_FILE, index=False)

    return metrics_dict

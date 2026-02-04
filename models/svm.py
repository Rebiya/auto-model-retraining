# =========================================
# File: models/svm.py
# Purpose: SVM classifier for churn prediction
# =========================================

import os
import sys
from pathlib import Path
import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import log_loss

# Ensure project root is on sys.path when running this file directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluate import evaluate_model
from src.plots import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_precision_recall_curve
)


class SVMModel:
    def __init__(
        self,
        kernel="rbf",
        C=1.0,
        gamma="scale",
        class_weight="balanced",
        probability=True,
        random_state=42
    ):
        """
        SVM classifier with probability estimates enabled for metrics/plots.
        """
        self.model = SVC(
            kernel=kernel,
            C=C,
            gamma=gamma,
            class_weight=class_weight,
            probability=probability,
            random_state=random_state
        )
        self.train_accuracy = None
        self.loss = None
        self.model_name = "svm"

    def train(self, X_train, y_train):
        """Fit the SVM on training data."""
        self.model.fit(X_train, y_train)

        self.train_accuracy = self.model.score(X_train, y_train)
        y_proba_train = self.model.predict_proba(X_train)
        self.loss = log_loss(y_train, y_proba_train)

        return self.model

    def predict(self, X):
        """Return class predictions."""
        return self.model.predict(X)

    def predict_proba(self, X):
        """Return predicted probabilities for positive class."""
        return self.model.predict_proba(X)[:, 1]

    def evaluate(self, X_test, y_test, model_name=None):
        """Compute metrics and generate plots."""
        name = model_name or self.model_name
        y_pred = self.predict(X_test)
        y_proba = self.predict_proba(X_test)

        metrics = evaluate_model(
            y_true=y_test,
            y_pred=y_pred,
            y_proba=y_proba,
            model_name=name,
            train_accuracy=self.train_accuracy,
            loss=self.loss
        )

        plot_confusion_matrix(y_test, y_pred, model_name=name)
        plot_roc_curve(y_test, y_proba, model_name=name)
        plot_precision_recall_curve(y_test, y_proba, model_name=name)

        return metrics

    def save_model(self, path="models/svm.joblib"):
        """Save trained SVM model."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        import joblib
        joblib.dump(self.model, path)

    def load_model(self, path="models/svm.joblib"):
        """Load trained SVM model."""
        import joblib
        self.model = joblib.load(path)


# # -------------------------------
# # Quick test / standalone usage
# # -------------------------------
# if __name__ == "__main__":
#     # Load preprocessed train/test
#     X_train = pd.read_csv("data/preprocessed/X_train.csv")
#     y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()
#     X_test = pd.read_csv("data/preprocessed/X_test.csv")
#     y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

#     svm_model = SVMModel(kernel="rbf", C=1.0, probability=True)

#     # Train
#     svm_model.train(X_train, y_train)

#     # Evaluate + save metrics + plots
#     metrics = svm_model.evaluate(X_test, y_test, model_name="svm")
#     print("SVM metrics:")
#     print(metrics)

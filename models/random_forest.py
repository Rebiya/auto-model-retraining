# =========================================
# File: models/random_forest.py
# Purpose: Random Forest classifier for churn prediction
# =========================================

import os
import sys
from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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


class RandomForestModel:
    def __init__(
        self,
        n_estimators=300,
        max_depth=8,
        min_samples_split=10,
        min_samples_leaf=4,
        max_features="sqrt",
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    ):
        """
        Random Forest optimized for imbalanced churn prediction.

        Key design goals:
        - Reduce overfitting from single Decision Tree
        - Improve recall (reduce false negatives)
        - Maintain strong AUC
        """

        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            max_features=max_features,
            class_weight=class_weight,
            random_state=random_state,
            n_jobs=n_jobs
        )

        self.model_name = "random_forest"

    def train(self, X_train, y_train):
        """Train the Random Forest model."""
        self.model.fit(X_train, y_train)
        self.train_accuracy = self.model.score(X_train, y_train)

        y_proba_train = self.model.predict_proba(X_train)
        self.loss = log_loss(y_train, y_proba_train)

    def evaluate(self, X_test, y_test, model_name=None):
        """
        Evaluate model, save metrics and plots.
        """
        name = model_name or self.model_name
        y_pred = self.model.predict(X_test)
        y_proba = self.model.predict_proba(X_test)[:, 1]

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

    def save_model(self, path="models/random_forest.joblib"):
        """Save trained model."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump(self.model, path)

    def load_model(self, path="models/random_forest.joblib"):
        """Load trained model."""
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

#     # Initialize model with hyperparameters
#     rf_model = RandomForestModel(
#         n_estimators=300,
#         max_depth=8,
#         min_samples_split=10,
#         min_samples_leaf=4,
#         max_features="sqrt",
#         class_weight="balanced",
#         random_state=42,
#         n_jobs=-1
#     )

#     # Train
#     rf_model.train(X_train, y_train)

#     # Evaluate + save metrics + plots
#     metrics = rf_model.evaluate(X_test, y_test, model_name="random_forest")
#     print("Random Forest metrics:")
#     print(metrics)

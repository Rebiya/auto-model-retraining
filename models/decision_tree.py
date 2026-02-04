# =========================================
# File: models/decision_tree.py
# Purpose: Train Decision Tree for Customer Churn
# Integrated with evaluate.py + plots.py
# =========================================

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import log_loss
import pandas as pd
import os
import sys
from pathlib import Path

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


class DecisionTreeModel:
    def __init__(
        self,
        max_depth=6,
        min_samples_split=10,
        min_samples_leaf=4,
        class_weight='balanced',
        random_state=42
    ):
        """
        Decision Tree Classifier with hyperparameters
        tuned to reduce overfitting.
        """
        self.model = DecisionTreeClassifier(
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf,
            random_state=random_state
        )
        self.train_accuracy = None
        self.loss = None

    def train(self, X_train, y_train):
        """Fit the decision tree on training data."""
        self.model.fit(X_train, y_train)

        # Optional: store training accuracy
        self.train_accuracy = self.model.score(X_train, y_train)

        # Optional: compute log loss (requires probability)
        y_proba_train = self.model.predict_proba(X_train)
        self.loss = log_loss(y_train, y_proba_train)

        return self.model

    def predict(self, X):
        """Return class predictions."""
        return self.model.predict(X)

    def predict_proba(self, X):
        """Return predicted probabilities for positive class."""
        return self.model.predict_proba(X)[:, 1]  # probability of class 1

    def evaluate(
        self,
        X_test,
        y_test,
        model_name="decision_tree"
    ):
        """Compute metrics and generate plots."""
        y_pred = self.predict(X_test)
        y_proba = self.predict_proba(X_test)

        # 1️⃣ Save metrics
        metrics = evaluate_model(
            y_true=y_test,
            y_pred=y_pred,
            y_proba=y_proba,
            model_name=model_name,
            train_accuracy=self.train_accuracy,
            loss=self.loss
        )

        # 2️⃣ Save plots
        plot_confusion_matrix(y_test, y_pred, model_name=model_name)
        plot_roc_curve(y_test, y_proba, model_name=model_name)
        plot_precision_recall_curve(y_test, y_proba, model_name=model_name)

        return metrics


# -------------------------------
# Quick test / standalone usage
# -------------------------------
# if __name__ == "__main__":
#     # Load preprocessed train/test
#     X_train = pd.read_csv("data/preprocessed/X_train.csv")
#     y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()
#     X_test = pd.read_csv("data/preprocessed/X_test.csv")
#     y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

#     # Initialize model with hyperparameters
#     dt_model = DecisionTreeModel(max_depth=6, min_samples_split=10, min_samples_leaf=4, class_weight='balanced', random_state=42)

#     # Train
#     dt_model.train(X_train, y_train)

#     # Evaluate + save metrics + plots
#     metrics = dt_model.evaluate(X_test, y_test, model_name="decision_tree")
#     print("Decision Tree metrics:")
#     print(metrics)

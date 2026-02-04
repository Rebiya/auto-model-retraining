# =========================================
# File: models/logistic_regression_sklearn.py
# Purpose: Logistic Regression (sklearn)
# =========================================

import sys
from pathlib import Path
import pandas as pd
from sklearn.linear_model import LogisticRegression

# ------------------------------------------------------------------
# Fix imports when running directly
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluate import evaluate_model
from src.plots import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_precision_recall_curve
)

# ------------------------------------------------------------------
# Logistic Regression Model Wrapper
# ------------------------------------------------------------------
class LogisticRegressionModel:
    def __init__(
        self,
        # C=0.5,
        # solver="liblinear",
        # class_weight="balanced",
        # max_iter=1000,
        # random_state=42,
        penalty="l2",
        C=1.5,
        solver="lbfgs",
        class_weight={0: 1.0, 1: 1.3},
        max_iter=2000,
        n_jobs=-1,
        random_state=42
    ):
        """
        Logistic Regression for churn prediction (binary).
        """
        self.model_name = "logistic_regression_sklearn"
        self.model = LogisticRegression(
            C=C,
            solver=solver,
            class_weight=class_weight,
            max_iter=max_iter,
            random_state=random_state
        )

        self.train_accuracy = None
        self.loss = None

    # ------------------------------------------------------------------
    # Train
    # ------------------------------------------------------------------
    def train(self, X_train, y_train):
        self.model.fit(X_train, y_train)

        # Training metrics
        self.train_accuracy = self.model.score(X_train, y_train)
        y_train_proba = self.model.predict_proba(X_train)
        from sklearn.metrics import log_loss
        self.loss = log_loss(y_train, y_train_proba)

        return self

    # ------------------------------------------------------------------
    # Predict
    # ------------------------------------------------------------------
    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)[:, 1]

    # ------------------------------------------------------------------
    # Evaluate + Save Metrics + Plots
    # ------------------------------------------------------------------
    def evaluate(self, X_test, y_test, model_name=None):
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

# # ------------------------------------------------------------------
# # Standalone execution (debug / local run)
# # ------------------------------------------------------------------
# if __name__ == "__main__":
#     X_train = pd.read_csv("data/preprocessed/X_train.csv")
#     y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()
#     X_test = pd.read_csv("data/preprocessed/X_test.csv")
#     y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

#     model = LogisticRegressionModel(
#         # C=0.5,
#         # solver="liblinear",
#         # class_weight="balanced",
#         # max_iter=1000
#         penalty="l2",
#         C=1.5,
#         solver="lbfgs",
#         class_weight={0: 1.0, 1: 1.3},
#         max_iter=2000,
#         n_jobs=-1,
#         random_state=42
#     )

#     model.train(X_train, y_train)
#     metrics = model.evaluate(X_test, y_test)

#     print("Logistic Regression metrics:")
#     print(metrics)

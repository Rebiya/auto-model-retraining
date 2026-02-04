# ======================================================
# File: models/logistic_regression_scratch.py
# Purpose: Logistic Regression from scratch (churn-optimized)
# ======================================================

import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, f1_score

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.evaluate import evaluate_model
from src.plots import (
    plot_confusion_matrix,
    plot_roc_curve,
    plot_precision_recall_curve
)


class LogisticRegressionScratch:
    def __init__(
        self,
        lr=0.01,
        epochs=3000,
        batch_size=128,
        l2_lambda=0.01,
        pos_weight=2.5,
        early_stopping=True,
        patience=25,
        random_state=42
    ):
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
        self.l2_lambda = l2_lambda
        self.pos_weight = pos_weight
        self.early_stopping = early_stopping
        self.patience = patience
        self.random_state = random_state

        self.w = None
        self.b = 0.0
        self.threshold = 0.5

        self.train_accuracy = None
        self.loss = None
        self.model_name = "logistic_regression_scratch"

    # -----------------------
    # Numerically stable sigmoid
    # -----------------------
    def _sigmoid(self, z):
        z = np.clip(z, -500, 500)
        return 1.0 / (1.0 + np.exp(-z))

    # -----------------------
    # Weighted log loss
    # -----------------------
    def _loss(self, y, p):
        eps = 1e-9
        p = np.clip(p, eps, 1 - eps)

        loss = (
            -self.pos_weight * y * np.log(p)
            - (1 - y) * np.log(1 - p)
        ).mean()

        # L2 penalty
        loss += self.l2_lambda * np.sum(self.w ** 2)
        return loss

    # -----------------------
    # Training
    # -----------------------
    def train(self, X, y):
        np.random.seed(self.random_state)

        X = X.values
        y = y.values

        X_tr, X_val, y_tr, y_val = train_test_split(
            X, y, test_size=0.2, stratify=y, random_state=self.random_state
        )

        n_samples, n_features = X_tr.shape
        self.w = np.zeros(n_features)

        best_auc = -np.inf
        patience_counter = 0

        for epoch in range(self.epochs):
            idx = np.random.permutation(n_samples)
            X_tr, y_tr = X_tr[idx], y_tr[idx]

            for start in range(0, n_samples, self.batch_size):
                end = start + self.batch_size
                xb = X_tr[start:end]
                yb = y_tr[start:end]

                z = xb @ self.w + self.b
                p = self._sigmoid(z)

                error = p - yb
                error[yb == 1] *= self.pos_weight

                dw = (xb.T @ error) / len(xb)
                db = error.mean()

                dw += 2 * self.l2_lambda * self.w

                self.w -= self.lr * dw
                self.b -= self.lr * db

            # ---- validation AUC for early stopping ----
            val_proba = self.predict_proba(pd.DataFrame(X_val))
            val_auc = roc_auc_score(y_val, val_proba)

            if self.early_stopping:
                if val_auc > best_auc:
                    best_auc = val_auc
                    patience_counter = 0
                else:
                    patience_counter += 1

                if patience_counter >= self.patience:
                    break

        # training metrics
        train_proba = self.predict_proba(pd.DataFrame(X))
        self.loss = self._loss(y, train_proba)
        self.train_accuracy = ((train_proba >= 0.5).astype(int) == y).mean()

        # tune threshold for best F1
        self._tune_threshold(X_val, y_val)

    # -----------------------
    # Threshold tuning (KEY!)
    # -----------------------
    def _tune_threshold(self, X_val, y_val):
        probs = self.predict_proba(pd.DataFrame(X_val))
        thresholds = np.linspace(0.2, 0.6, 50)

        best_f1 = -1
        best_t = 0.5

        for t in thresholds:
            preds = (probs >= t).astype(int)
            f1 = f1_score(y_val, preds)

            if f1 > best_f1:
                best_f1 = f1
                best_t = t

        self.threshold = best_t

    # -----------------------
    def predict_proba(self, X):
        return self._sigmoid(X.values @ self.w + self.b)

    def predict(self, X):
        return (self.predict_proba(X) >= self.threshold).astype(int)

    # -----------------------
    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        y_proba = self.predict_proba(X_test)

        metrics = evaluate_model(
            y_true=y_test,
            y_pred=y_pred,
            y_proba=y_proba,
            model_name=self.model_name,
            train_accuracy=self.train_accuracy,
            loss=self.loss
        )

        plot_confusion_matrix(y_test, y_pred, model_name=self.model_name)
        plot_roc_curve(y_test, y_proba, model_name=self.model_name)
        plot_precision_recall_curve(y_test, y_proba, model_name=self.model_name)

        return metrics


# -----------------------
# Standalone run
# -----------------------
if __name__ == "__main__":
    X_train = pd.read_csv("data/preprocessed/X_train.csv")
    y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()
    X_test = pd.read_csv("data/preprocessed/X_test.csv")
    y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

    model = LogisticRegressionScratch(
        lr=0.01,
        epochs=3000,
        batch_size=128,
        l2_lambda=0.01,
        pos_weight=2.5
    )

    model.train(X_train, y_train)
    metrics = model.evaluate(X_test, y_test)

    print("Scratch Logistic Regression metrics:")
    print(metrics)

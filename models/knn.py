import os
import sys
from pathlib import Path
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
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


class KNNModel:
    def __init__(
        self,
        n_neighbors=55,
        weights="uniform",
        metric="manhattan",
        p=1
    ):
        self.model = KNeighborsClassifier(
            n_neighbors=n_neighbors,
            weights=weights,
            metric=metric,
            p=p
        )
        self.train_accuracy = None
        self.loss = None
        self.model_name = "knn"

    def train(self, X_train, y_train):
        """Fit the KNN model on training data."""
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


# if __name__ == "__main__":
#     # Load processed data
#     X_train = pd.read_csv("data/preprocessed/X_train.csv")
#     y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()

#     X_test = pd.read_csv("data/preprocessed/X_test.csv")
#     y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

#     knn_model = KNNModel(n_neighbors=55, weights="uniform", metric="manhattan", p=1)
#     knn_model.train(X_train, y_train)
#     metrics = knn_model.evaluate(X_test, y_test, model_name="knn")
#     print("KNN metrics:")
#     print(metrics)

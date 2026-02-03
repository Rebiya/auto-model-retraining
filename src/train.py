# =========================================
# File: src/train.py
# Purpose: Train all models on original preprocessed data
# =========================================

import pandas as pd
import os

# Import all models
from models.decision_tree import DecisionTreeModel
from models.knn import KNNModel
from models.logistic_regression_scratch import LogisticRegressionScratch
from models.logistic_regression_sklearn import LogisticRegressionSklearn
from models.random_forest import RandomForestModel
from models.svm import SVMModel


def main():
    # ------------------------------
    # 1️⃣ Load original preprocessed data
    # ------------------------------
    X_train = pd.read_csv("data/preprocessed/X_train.csv")
    y_train = pd.read_csv("data/preprocessed/y_train.csv").squeeze()
    X_test = pd.read_csv("data/preprocessed/X_test.csv")
    y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

    # ------------------------------
    # 2️⃣ Initialize all models
    # ------------------------------
    models = {
        "decision_tree": DecisionTreeModel(max_depth=7, min_samples_split=5, min_samples_leaf=2),
        "knn": KNNModel(n_neighbors=5),
        "logistic_regression_scratch": LogisticRegressionScratch(lr=0.01, n_iter=5000),
        "logistic_regression_sklearn": LogisticRegressionSklearn(),
        "random_forest": RandomForestModel(n_estimators=100, max_depth=7),
        "svm": SVMModel(kernel="rbf", C=1.0, probability=True)
    }

    # ------------------------------
    # 3️⃣ Train + Evaluate all models
    # ------------------------------
    for name, model in models.items():
        print(f"\n=== Training {name} ===")
        model.train(X_train, y_train)
        metrics = model.evaluate(X_test, y_test, model_name=name)
        print(metrics)

    print("\nAll models trained and evaluated successfully.")


if __name__ == "__main__":
    main()

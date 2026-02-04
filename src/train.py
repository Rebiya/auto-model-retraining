# Purpose: Train all models on original preprocessed data
# to run use: python src/train.py
# =========================================

import os
import sys
from pathlib import Path
import pandas as pd
import os

# Ensure project root is on sys.path when running this file directly.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import all models
from models.decision_tree import DecisionTreeModel
from models.knn import KNNModel
from models.logistic_regression_scratch import LogisticRegressionScratch
from models.logistic_regression_sklearn import LogisticRegressionModel
from models.random_forest import RandomForestModel
from models.svm import SVMModel

def initial_training():
    """
    Initial training on preprocessed data (run once)
    """
    print("🏁 Initial training started")
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
        "decision_tree": DecisionTreeModel(max_depth=6, min_samples_split=10, min_samples_leaf=4, class_weight='balanced', random_state=42),
        "knn": KNNModel(n_neighbors=55, weights="uniform", metric="manhattan", p=1),
        "logistic_regression_scratch": LogisticRegressionScratch(lr=0.01,epochs=3000,batch_size=128,l2_lambda=0.01, pos_weight=2.5),
        "logistic_regression_sklearn": LogisticRegressionModel(
        # C=0.5,
        # solver="liblinear",
        # class_weight="balanced",
        # max_iter=1000
        penalty="l2",
        C=1.5,
        solver="lbfgs",
        class_weight={0: 1.0, 1: 1.3},
        max_iter=2000,
        n_jobs=-1,
        random_state=42
    ),
        "random_forest": RandomForestModel(
        n_estimators=300,
        max_depth=8,
        min_samples_split=10,
        min_samples_leaf=4,
        max_features="sqrt",
        class_weight="balanced",
        random_state=42,
        n_jobs=-1
    ),
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
    print("✅ Initial training completed")

# if __name__ == "__main__":
#     initial_training()
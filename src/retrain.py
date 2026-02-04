# =========================================
# File: src/retrain.py
# Purpose: Retrain all models using latest combined dataset + new augmentation
# to run use: python -m src.retrain
# =========================================
import os
import sys
from pathlib import Path
import pandas as pd
import os
import re

from src.augment import augment_data

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


def get_latest_combined_version(combined_dir="data/combined"):
    """Return the max version number of combined dataset, -1 if none exists."""
    if not os.path.exists(combined_dir):
        os.makedirs(combined_dir)
        return -1
    pattern = re.compile(r"X_train_combined_(\d+)\.csv")
    versions = [int(pattern.match(f).group(1)) for f in os.listdir(combined_dir) if pattern.match(f)]
    return max(versions) if versions else -1


def main():
    # ------------------------------
    # 1️⃣ Load original processed data for augmentation
    # ------------------------------
    X_orig = pd.read_csv("data/preprocessed/X_train.csv")
    y_orig = pd.read_csv("data/preprocessed/y_train.csv").squeeze()

    # ------------------------------
    # 2️⃣ Generate augmented data
    # ------------------------------
    X_aug, y_aug = augment_data(X_orig, y_orig, n_samples=500)

    # ------------------------------
    # 3️⃣ Load latest combined dataset if exists, else start from original
    # ------------------------------
    latest_version = get_latest_combined_version()
    combined_dir = "data/combined"

    if latest_version == -1:
        print("No previous combined data found. Starting from original processed data.")
        X_combined_base = X_orig
        y_combined_base = y_orig
        new_version = 0
    else:
        print(f"Loading latest combined dataset version: {latest_version}")
        X_combined_base = pd.read_csv(os.path.join(combined_dir, f"X_train_combined_{latest_version}.csv"))
        y_combined_base = pd.read_csv(os.path.join(combined_dir, f"y_train_combined_{latest_version}.csv")).squeeze()
        new_version = latest_version + 1

    # ------------------------------
    # 4️⃣ Combine base + current augmented
    # ------------------------------
    X_train_combined = pd.concat([X_combined_base, X_aug], ignore_index=True)
    y_train_combined = pd.concat([y_combined_base, y_aug], ignore_index=True)

    # ------------------------------
    # 5️⃣ Save new combined dataset
    # ------------------------------
    os.makedirs(combined_dir, exist_ok=True)
    X_train_combined.to_csv(os.path.join(combined_dir, f"X_train_combined_{new_version}.csv"), index=False)
    y_train_combined.to_csv(os.path.join(combined_dir, f"y_train_combined_{new_version}.csv"), index=False)
    print(f"Saved combined dataset version {new_version}")

    # ------------------------------
    # 6️⃣ Load test set (unchanged)
    # ------------------------------
    X_test = pd.read_csv("data/preprocessed/X_test.csv")
    y_test = pd.read_csv("data/preprocessed/y_test.csv").squeeze()

    # ------------------------------
    # 7️⃣ Initialize models
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
    # 8️⃣ Train + Evaluate on latest combined dataset
    # ------------------------------
    for name, model in models.items():
        print(f"\n=== Retraining {name} on combined dataset version {new_version} ===")
        model.train(X_train_combined, y_train_combined)
        metrics = model.evaluate(X_test, y_test, model_name=name)
        print(metrics)

    print("\nRetraining completed successfully.")


if __name__ == "__main__":
    main()

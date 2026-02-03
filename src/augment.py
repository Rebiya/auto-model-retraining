# =========================================
# File: src/augment.py
# Purpose: Incrementally generate augmented Customer Churn training data
# Combine with original processed training data or most recent combined dataset
# Numeric versioning for saving
# =========================================

import pandas as pd
import numpy as np
import os
import re

def augment_data(X_base: pd.DataFrame, y_base: pd.Series, n_samples: int = 500, random_state: int = 42):
    """
    Generate augmented samples from the provided base dataset.

    Parameters
    ----------
    X_base : pd.DataFrame
        Base features to augment (original processed or latest combined)
    y_base : pd.Series
        Base targets
    n_samples : int
        Number of augmented samples to generate
    random_state : int
        Random seed

    Returns
    -------
    X_aug : pd.DataFrame
        Newly augmented features
    y_aug : pd.Series
        Newly augmented targets
    """
    np.random.seed(random_state)

    X_rows, y_rows = [], []

    categorical_cols = X_base.select_dtypes(include=['object']).columns.tolist()
    numerical_cols = X_base.select_dtypes(include=['int64','float64']).columns.tolist()

    num_stats = X_base[numerical_cols].describe().T
    num_std = num_stats['std']

    cat_distributions = {col: X_base[col].value_counts(normalize=True) for col in categorical_cols}
    target_probs = y_base.value_counts(normalize=True)

    for i in range(n_samples):
        num_row = {col: max(
            X_base[col].sample(1, random_state=random_state+i).values[0] +
            np.random.normal(0, 0.1 * num_std[col]), 0)
                   for col in numerical_cols}
        cat_row = {col: np.random.choice(cat_distributions[col].index, p=cat_distributions[col].values)
                   for col in categorical_cols}

        X_rows.append({**num_row, **cat_row})
        y_rows.append(np.random.choice(target_probs.index, p=target_probs.values))

    X_aug = pd.DataFrame(X_rows, columns=X_base.columns)
    y_aug = pd.Series(y_rows, dtype=y_base.dtype)

    return X_aug, y_aug


def get_next_version(folder_path: str, prefix: str = "X_train_combined_") -> int:
    """Get the next numeric version for saving combined dataset."""
    if not os.path.exists(folder_path):
        return 0
    existing = [f for f in os.listdir(folder_path) if f.startswith(prefix) and f.endswith(".csv")]
    numbers = [int(re.search(rf"{prefix}(\d+)\.csv", f).group(1)) for f in existing
               if re.search(rf"{prefix}(\d+)\.csv", f)]
    return max(numbers) + 1 if numbers else 0


def get_latest_combined(folder_path: str, prefix: str = "X_train_combined_"):
    """Return the most recent combined dataset (X, y) if exists, else None."""
    if not os.path.exists(folder_path):
        return None, None, -1
    existing = [f for f in os.listdir(folder_path) if f.startswith(prefix) and f.endswith(".csv")]
    if not existing:
        return None, None, -1
    numbers = [(int(re.search(rf"{prefix}(\d+)\.csv", f).group(1)), f) for f in existing]
    max_version, latest_file = max(numbers, key=lambda x: x[0])
    X_latest = pd.read_csv(os.path.join(folder_path, latest_file))
    y_file = f"y_train_combined_{max_version}.csv"
    y_latest = pd.read_csv(os.path.join(folder_path, y_file)).squeeze()
    return X_latest, y_latest, max_version


if __name__ == "__main__":
    combined_folder = "data/combined"
    os.makedirs(combined_folder, exist_ok=True)

    # Load original processed data for augmentation
    X_original = pd.read_csv("data/preprocessed/X_train.csv")
    y_original = pd.read_csv("data/preprocessed/y_train.csv").squeeze()

    # Check if combined folder has previous versions
    X_latest, y_latest, latest_version = get_latest_combined(combined_folder)

    # Augmentation always uses original processed data
    X_aug, y_aug = augment_data(X_original, y_original, n_samples=500)

    # Determine base to combine with augmented
    if latest_version == -1:
        # No previous combined dataset → first version
        X_combined = pd.concat([X_original, X_aug], ignore_index=True)
        y_combined = pd.concat([y_original, y_aug], ignore_index=True)
        next_version = 0
    else:
        # Incremental: most recent combined + new augmented
        X_combined = pd.concat([X_latest, X_aug], ignore_index=True)
        y_combined = pd.concat([y_latest, y_aug], ignore_index=True)
        next_version = latest_version + 1

    # Save combined dataset with numeric versioning
    X_combined.to_csv(f"{combined_folder}/X_train_combined_{next_version}.csv", index=False)
    y_combined.to_csv(f"{combined_folder}/y_train_combined_{next_version}.csv", index=False)

    print(f"Combined dataset saved as version {next_version}. Preview:")
    print(X_combined.tail())
    print(y_combined.value_counts(normalize=True))

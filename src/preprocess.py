# =========================================
# File: src/preprocess.py
# Purpose: Preprocess raw churn data into train/test sets
# =========================================

import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


def preprocess_pipeline():
    print("🧹 Preprocessing raw data")

    # File path
    data_path = os.path.join(os.path.dirname(__file__), "../data/customer_churn.csv")
    data_path = os.path.abspath(data_path)

    if not os.path.exists(data_path):
        raise FileNotFoundError(
            f"Data file not found at {data_path}. Please check the path and ensure the file exists."
        )

    # Load CSV
    df = pd.read_csv(data_path)

    # Drop customerID
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)

    # Convert TotalCharges to numeric (coerce errors to NaN)
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    # Separate target and features
    X = df.drop("Churn", axis=1)
    y = df["Churn"].map({"Yes": 1, "No": 0})

    # Train-test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Identify categorical and numerical features
    categorical_cols = X_train.select_dtypes(include=["object"]).columns.tolist()
    numerical_cols = X_train.select_dtypes(include=["int64", "float64"]).columns.tolist()

    # Numerical pipeline: impute missing -> scale
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    # Categorical pipeline: impute missing -> one-hot encode
    cat_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    # Full preprocessor
    preprocessor = ColumnTransformer([
        ("num", num_pipeline, numerical_cols),
        ("cat", cat_pipeline, categorical_cols)
    ])

    # Fit preprocessor on training data only
    X_train_processed = preprocessor.fit_transform(X_train)

    # Transform test data (no fitting)
    X_test_processed = preprocessor.transform(X_test)

    # Save outputs
    os.makedirs("data/preprocessed", exist_ok=True)

    X_train_out = "data/preprocessed/X_train.csv"
    X_test_out = "data/preprocessed/X_test.csv"
    y_train_out = "data/preprocessed/y_train.csv"
    y_test_out = "data/preprocessed/y_test.csv"
    preprocessor_out = "data/preprocessed/preprocessor.joblib"

    pd.DataFrame(
        X_train_processed.toarray() if hasattr(X_train_processed, "toarray") else X_train_processed
    ).to_csv(X_train_out, index=False)

    pd.DataFrame(
        X_test_processed.toarray() if hasattr(X_test_processed, "toarray") else X_test_processed
    ).to_csv(X_test_out, index=False)

    y_train.to_csv(y_train_out, index=False)
    y_test.to_csv(y_test_out, index=False)

    joblib.dump(preprocessor, preprocessor_out)

    print("✅ Preprocessing done")

    return {
        "X_train": X_train_out,
        "X_test": X_test_out,
        "y_train": y_train_out,
        "y_test": y_test_out,
        "preprocessor": preprocessor_out
    }

# if __name__ == "__main__":
#     preprocess_pipeline()
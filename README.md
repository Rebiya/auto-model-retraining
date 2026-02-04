# Automated Model Retraining 

## Project Overview

This project implements a **production-style machine learning training system** for binary classification using the Telco Customer Churn dataset. It supports **initial training**, **scheduled retraining with data augmentation**, **model comparison**, and **automatic evaluation and visualization** — all orchestrated from a single entry point.

The system is designed to resemble a real-world ML workflow where models continuously improve as new (or augmented) data becomes available.

---

## Key Features

* End-to-end ML pipeline (preprocess → train → evaluate → retrain)
* Single unified entry point (`main.py`)
* Periodic retraining using **Celery Beat (scheduler)**
* Data augmentation for retraining robustness
* Multiple models (tree-based, distance-based, margin-based, linear)
* From-scratch Logistic Regression implementation
* Centralized metrics logging (`results.csv`)
* Automatic generation of ROC, PR, and confusion matrix plots

---

## Models Implemented

| Model                         | Description                                                   |
| ----------------------------- | ------------------------------------------------------------- |
| Logistic Regression (Scratch) | Fully manual gradient descent, regularization, early stopping |
| Logistic Regression (Sklearn) | Baseline linear classifier                                    |
| KNN                           | Distance-based with tuned neighbors                           |
| SVM                           | Margin-based classifier with RBF kernel                       |
| Decision Tree                 | Depth & leaf constrained to prevent overfitting               |
| Random Forest                 | Ensemble of de-correlated decision trees                      |

---

## Folder Structure 

```
auto-model-retraining/
│
├── data/
│   ├── customer_churn.csv          # Raw dataset
│   ├── preprocessed/               # Saved processed splits
│   │   ├── X_train.csv
│   │   ├── X_test.csv
│   │   ├── y_train.csv
│   │   ├── y_test.csv
│   │   └── preprocessor.joblib
│   └── combined/                   # Augmented + original training data
│
├── models/                          # Model definitions only (no training)
│   ├── decision_tree.py
│   ├── random_forest.py
│   ├── svm.py
│   ├── knn.py
│   ├── logistic_regression_scratch.py
│   └── logistic_regression_sklearn.py
│
├── src/
│   ├── preprocess.py               # Data cleaning, encoding, scaling
│   ├── augment.py                  # Synthetic data generation
│   ├── train.py                    # Model fitting logic
│   ├── evaluate.py                 # Metrics computation
│   ├── plots.py                    # ROC, PR, confusion matrix plots
│   ├── retrain.py                  # Augment → retrain → evaluate
│   ├── celery_app.py               # Celery configuration
│   └── tasks.py                    # Scheduled retraining tasks
│
├── figures/                         # Auto-generated plots per model
│   ├── decision_tree/
│   ├── random_forest/
│   ├── svm/
│   ├── knn/
│   ├── logistic_regression_scratch/
│   └── logistic_regression_sklearn/
│
├── reports/
│   └── final_report.pdf
│
├── results.csv                     # Centralized metrics store
├── main.py                         # Single unified entry point
├── requirements.txt
└── README.md
```

---

## Execution Flow

### 1. Start the system

```bash
python main.py
```

This launches the **entire pipeline** and keeps the process alive so scheduled retraining can occur.

---

### 2. Initial Training Phase

```text
customer_churn.csv
    ↓
preprocess.py
    ↓
X_train, X_test, y_train, y_test
    ↓
train.py
    ↓
evaluate.py → results.csv + figures/
```

---

### 3. Scheduled Retraining (Every 5 Minutes)

Handled automatically by **Celery Beat** while `main.py` is running.

```text
X_train, y_train
    ↓
augment.py
    ↓
preprocessing_pipeline.transform
    ↓
merge combined(original+recent combined) + augmented data
    ↓
train.py
    ↓
evaluate.py → append results.csv + new plots
```

---

## Visual Pipeline Diagram

```
data/customer_churn.csv
        │
        ▼
   preprocess.py
        │
   X_train, X_test, y_train, y_test
        │
        ▼
   train.py  ──► models/*.py
        │
        ▼
   evaluate.py ──► results.csv + figures/
        │
        ▼
   augment.py
        │
        ▼
   retrain.py (scheduled via Celery)
```

---

## How Retraining Works

* `main.py` initializes preprocessing and first training round
* Celery Beat schedules `retrain_model()` every **5 minutes**
* Data augmentation using the same scaler & encoder
* Models are retrained and evaluated automatically
* Metrics are appended (not overwritten)

---

## Requirements

```bash
pip install -r requirements.txt
```

Required services:

* Python 3.10+
* Redis (for Celery broker)

Start Redis locally:

```bash
redis-server
```
To start the app run: 
```bash 
python main.py
```
---

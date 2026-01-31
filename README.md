# 🔹 Final Folder & File Flow Diagram 

```
classification-retraining-project/
│
├── data/
│   └── customer_churn.csv
│        │
        ▼
├── src/
│   ├── preprocess.py
│   │     - Load raw CSV 
│   │     - Handle missing values
│   │     - Encode categorical features
│   │     - Scale numerical features
│   │     - Train/test split
│   │     - Returns: X_train, X_test, y_train, y_test, preprocessing_pipeline
│   │
│   ├── augment.py
│   │     - Generate synthetic data (bootstrapping/noise)
│   │     - Returns: X_aug, y_aug
│   │
│   ├── models/
│   │     ├── logistic_regression_scratch.py   <-- from scratch
│   │     ├── logistic_regression_sklearn.py
│   │     ├── knn.py
│   │     ├── svm.py
│   │     ├── decision_tree.py
│   │     └── random_forest.py
│   │     - Each file: define/get model, no training
│   │
│   ├── train.py
│   │     - Accepts models + training data
│   │     - Fits models
│   │     - Returns trained models
│   │
│   ├── evaluate.py
│   │     - Accepts trained models + test data
│   │     - Generates predictions
│   │     - Calculates metrics (accuracy, precision, recall, F1)
│   │     - Saves metrics to root results.csv
│   │     - Calls plots.py for visualizations
│   │
│   ├── plots.py
│   │     - Confusion matrix, ROC, metric bar plots
│   │     - Saves figures inside model-specific folders with timestamp + training round
│   │
│   └── retrain.py
│         - Calls augment.py
│         - Preprocess augmented data using preprocessing_pipeline
│         - Merges augmented data with original training data
│         - Calls train.py on combined data
│         - Calls evaluate.py on retrained models
│
├── figures/                  <-- Model-specific figure folders
│   ├── logistic_regression_scratch/
│   ├── logistic_regression_sklearn/
│   ├── knn/
│   ├── svm/
│   ├── decision_tree/
│   └── random_forest/
│
├── results.csv               <-- Root: metrics per model + training round
├── reports/
│   └── final_report.pdf
├── requirements.txt
├── README.md
└── main.py                   <-- Single entry point

```

---

### Root Level

```
results.csv        <-- Stores metrics: timestamp, training_round, model, accuracy, precision, recall, F1
figures/           <-- Model-specific folders: all plots saved here
reports/final_report.pdf  <-- Final report
main.py            <-- Orchestrates entire workflow
requirements.txt
README.md
```

---

# 🔹 **Flow of Execution (Step-by-Step)**

1️⃣ **Start `main.py`**

2️⃣ **Load & preprocess original data**

```text
customer_churn.csv → preprocess.py → X_train, X_test, y_train, y_test, preprocessing_pipeline
```

3️⃣ **Train initial models**

```text
models/* → train.py → trained_models_round1
```

4️⃣ **Evaluate initial models**

```text
trained_models_round1 + X_test → evaluate.py → results.csv + figures/*
```

5️⃣ **Generate augmented data**

```text
X_train, y_train → augment.py → X_aug, y_aug
```

6️⃣ **Preprocess augmented data**

```text
X_aug → preprocessing_pipeline.transform(X_aug) → X_aug_processed
```

7️⃣ **Merge augmented + original training data**

```text
X_train + X_aug_processed → X_combined
y_train + y_aug → y_combined
```

8️⃣ **Retrain models on combined data**

```text
X_combined, y_combined → train.py → trained_models_round2
```

9️⃣ **Evaluate retrained models**

```text
trained_models_round2 + X_test → evaluate.py → append to results.csv + save new figures in model folders
```

10️⃣ **Results ready for report**

* `results.csv` → tables
* `figures/` → plots
* `reports/final_report.pdf` → final submission


# 🔹 Visual Concept (text diagram)

```
data/customer_churn.csv
        │
        ▼
   preprocess.py
        │
   X_train, X_test, y_train, y_test
        │
        ▼
   train.py  ──► models/*.py ──► trained_models
        │
        ▼
   evaluate.py ──► results.csv + plots.py ──► figures/
        │
        ▼
   augment.py ──► X_aug, y_aug
        │
        ▼
   preprocess.py ──► X_aug_processed
        │
        ▼
   retrain.py ──► train.py + evaluate.py → updated results.csv + updated figures
```


---


# 🔹 Notes

* Preprocessing is **shared** for original and augmented data → keeps distributions consistent
* Figures are **timestamped + round-specific** → shows retraining effect
* Models are **modular** → one file per model, scratch LR included
* `results.csv` keeps metrics **centralized and reproducible**

Perfect — let’s make this **crystal clear**, minimal, and competition-ready. I’ll draw a **flow diagram showing all files, folders, and how augmented data is handled**.


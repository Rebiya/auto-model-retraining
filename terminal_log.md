### 🖥️ System Execution Logs

```text
🚀 Auto Model Retraining System Started
🧹 Preprocessing raw data... ✅ Done
🏁 Initial training started

=== Training decision_tree ===
{'model': 'decision_tree', 'train_accuracy': 0.8085, 'test_accuracy': 0.7928, 'loss': 0.3891, 'f1_score': 0.5642, 'roc_auc_score': 0.8364}

=== Training knn ===
{'model': 'knn', 'train_accuracy': 0.8080, 'test_accuracy': 0.7814, 'loss': 0.4155, 'f1_score': 0.5838, 'roc_auc_score': 0.8298}

=== Training logistic_regression_scratch ===
{'model': 'logistic_regression_scratch', 'train_accuracy': 0.7623, 'test_accuracy': 0.7637, 'loss': 0.6953, 'f1_score': 0.6186, 'roc_auc_score': 0.8390}

=== Training logistic_regression_sklearn ===
{'model': 'logistic_regression_sklearn', 'train_accuracy': 0.7987, 'test_accuracy': 0.7828, 'loss': 0.4173, 'f1_score': 0.6047, 'roc_auc_score': 0.8418}

=== Training random_forest ===
{'model': 'random_forest', 'train_accuracy': 0.7936, 'test_accuracy': 0.7580, 'loss': 0.4190, 'f1_score': 0.6321, 'roc_auc_score': 0.8419}

=== Training svm ===
{'model': 'svm', 'train_accuracy': 0.7725, 'test_accuracy': 0.7438, 'loss': 0.3999, 'f1_score': 0.6155, 'roc_auc_score': 0.8211}

✅ Initial training completed
🚀 Starting Celery worker & Beat scheduler...
✅ System is live. Retraining every 5 minutes.

[2026-02-04 15:10:00] 🔁 Celery triggered retraining...
[2026-02-04 15:10:08] Saved combined dataset version 3

=== Retraining decision_tree on version 3 ===
{'model': 'decision_tree', 'test_accuracy': 0.7921, 'f1_score': 0.4869, 'roc_auc_score': 0.8261}
=== Retraining knn on version 3 ===
{'model': 'knn', 'test_accuracy': 0.7828, 'f1_score': 0.5616, 'roc_auc_score': 0.8224}
=== Retraining logistic_regression_scratch on version 3 ===
{'model': 'logistic_regression_scratch', 'test_accuracy': 0.7530, 'f1_score': 0.6116, 'roc_auc_score': 0.8345}
=== Retraining logistic_regression_sklearn on version 3 ===
{'model': 'logistic_regression_sklearn', 'test_accuracy': 0.7963, 'f1_score': 0.5894, 'roc_auc_score': 0.8357}
=== Retraining random_forest on version 3 ===
{'model': 'random_forest', 'test_accuracy': 0.7516, 'f1_score': 0.6300, 'roc_auc_score': 0.8430}
=== Retraining svm on version 3 ===
{'model': 'svm', 'test_accuracy': 0.7445, 'f1_score': 0.6170, 'roc_auc_score': 0.8193}

✅ Retraining finished (Duration: 32.43s)

[2026-02-04 15:15:00] 🔁 Celery triggered retraining...
[2026-02-04 15:15:09] Saved combined dataset version 4

=== Retraining decision_tree on version 4 ===
{'model': 'decision_tree', 'test_accuracy': 0.7921, 'f1_score': 0.4869, 'roc_auc_score': 0.8221}
=== Retraining knn on version 4 ===
{'model': 'knn', 'test_accuracy': 0.7835, 'f1_score': 0.5573, 'roc_auc_score': 0.8195}
=== Retraining logistic_regression_scratch on version 4 ===
{'model': 'logistic_regression_scratch', 'test_accuracy': 0.7473, 'f1_score': 0.6130, 'roc_auc_score': 0.8352}
=== Retraining logistic_regression_sklearn on version 4 ===
{'model': 'logistic_regression_sklearn', 'test_accuracy': 0.7942, 'f1_score': 0.5797, 'roc_auc_score': 0.8333}
=== Retraining random_forest on version 4 ===
{'model': 'random_forest', 'test_accuracy': 0.7523, 'f1_score': 0.6307, 'roc_auc_score': 0.8433}
=== Retraining svm on version 4 ===
{'model': 'svm', 'test_accuracy': 0.7488, 'f1_score': 0.6185, 'roc_auc_score': 0.8179}

✅ Retraining finished (Duration: 38.63s)

[2026-02-04 15:20:00] 🔁 Celery triggered retraining...
[2026-02-04 15:20:09] Saved combined dataset version 5

=== Retraining decision_tree on version 5 ===
{'model': 'decision_tree', 'test_accuracy': 0.7949, 'f1_score': 0.5434, 'roc_auc_score': 0.8195}
=== Retraining knn on version 5 ===
{'model': 'knn', 'test_accuracy': 0.7814, 'f1_score': 0.5484, 'roc_auc_score': 0.8177}
=== Retraining logistic_regression_scratch on version 5 ===
{'model': 'logistic_regression_scratch', 'test_accuracy': 0.7353, 'f1_score': 0.6061, 'roc_auc_score': 0.8318}
=== Retraining logistic_regression_sklearn on version 5 ===
{'model': 'logistic_regression_sklearn', 'test_accuracy': 0.7949, 'f1_score': 0.5769, 'roc_auc_score': 0.8309}
=== Retraining random_forest on version 5 ===
{'model': 'random_forest', 'test_accuracy': 0.7445, 'f1_score': 0.6250, 'roc_auc_score': 0.8419}
=== Retraining svm on version 5 ===
{'model': 'svm', 'test_accuracy': 0.7480, 'f1_score': 0.6170, 'roc_auc_score': 0.8163}

✅ Retraining finished (Duration: 42.90s)

^C🛑 Shutting down system...
worker: Warm shutdown complete.
# src/tasks.py
from src.celery_app import celery_app
from src.retrain import retrain_pipeline

@celery_app.task
def retrain_models():
    print("🔁 Celery triggered retraining...")
    retrain_pipeline()

# src/celery_app.py
from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "auto_model_retraining",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
    include=["src.tasks"]
)

celery_app.conf.update(
    timezone="UTC",
    beat_schedule={
        "retrain-every-5-minutes": {
            "task": "src.tasks.retrain_models",
            "schedule": crontab(minute="*/5"),
        }
    }
)

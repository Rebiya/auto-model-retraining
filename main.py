# main.py
import subprocess
import time
import sys
from src.preprocess import preprocess_pipeline
from src.train import initial_training

def start_celery():
    print("🚀 Starting Celery worker...")
    subprocess.Popen(
        ["celery", "-A", "src.celery_app", "worker", "--loglevel=info"]
    )

    print("⏱️ Starting Celery beat scheduler...")
    subprocess.Popen(
        ["celery", "-A", "src.celery_app", "beat", "--loglevel=info"]
    )

if __name__ == "__main__":
    print("🚀 Auto Model Retraining System Started")

    # 1️⃣ Preprocess
    preprocess_pipeline()

    # 2️⃣ Initial training
    initial_training()

    # 3️⃣ Start Celery worker + scheduler
    start_celery()

    # 4️⃣ Keep main alive
    print("✅ System is live. Retraining every 5 minutes.")
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Shutting down system")
        sys.exit(0)

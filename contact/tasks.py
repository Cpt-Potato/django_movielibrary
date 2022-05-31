from django_movielibrary.celery import app
from .services import send_confirm_subscription


@app.task
def send_confirm_subscription_task(user_email):
    send_confirm_subscription(user_email)

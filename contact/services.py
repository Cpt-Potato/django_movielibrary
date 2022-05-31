from django.core.mail import send_mail

from django_movielibrary.settings import FROM_EMAIL


def send_confirm_subscription(user_email):
    send_mail(
        'Вы подписались на рассылку',
        'Мы будем периодически присылать вам письма',
        FROM_EMAIL,
        [user_email]
    )

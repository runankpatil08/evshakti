from django.core.mail import send_mail
from django.conf import settings

def send_user_email(to_email, subject, message):
    """Reusable function to send Gmail alerts"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )

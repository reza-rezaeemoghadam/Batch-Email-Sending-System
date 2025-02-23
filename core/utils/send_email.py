from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_batch_email(email_list:list, subject:str, body:str) -> str:
    """
    Task to send emails in batch asynchronously.
    """
    for email in email_list:
        send_mail(subject, body, settings.EMAIL_HOST_USER, [email])
    return f"Send {len(email_list)} emails."

@shared_task
def send_single_email(email:str, subject:str, body:str) -> str:
    send_mail(subject, body, settings.EMAIL_HOST_USER, [email])
    return f"Email sent to {email}"
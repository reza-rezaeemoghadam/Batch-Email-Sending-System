import os
from decouple import config
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('DJANGO_SETTINGS_MODULE', cast=str))
app = Celery('src')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
from decouple import config

print(config("CELERY_ACCEPT_CONTENT", cast=list))
print(config("CELERY_TASK_SERIALIZER"))
print(config("CELERY_BROKER_URL", cast=str))
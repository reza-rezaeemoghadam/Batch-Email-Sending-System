from decouple import config

print(config("CELERY_ACCEPT_CONTENT", cast=list))
print(config("CELERY_TASK_SERIALIZER"))
# Importing extra modules
import os

from core.utils.csv_to_list import convert_csv_to_list
# Importing base settings
from src.base import *

# Importing extra modules
from datetime import timedelta

# Swagger configuration
SPECTACULAR_SETTINGS = {
    'TITLE': 'Batch Email API',
    'SCHEMA_PATH_PREFIX': '/api/v1',  # Ensure only API routes are documented
    'DESCRIPTION': 'Queue practice API Documentation.',
    'SWAGGER_UI_SETTINGS': {
        'tryItOutEnabled': True,
        'displayRequestDuration': True,
        'docExpansion': 'none',
    },
    'SWAGGER_UI_SETTINGS': {
        'docExpansion': 'none',
    },
    'SECURITY': [
        {'BearerAuth': []}
    ],
    'SERVERS': [
        {'url': config("SWAGGER_LOCAL_URL", cast=str), 'description': 'Local Development Server'},
        {'url': config("SWAGGER_DEVELOPMENT_URL", cast=str), 'description': 'Development Server'},
        {'url': config("SWAGGER_DEPLOYMENT_URL", cast=str), 'description': 'Production Server'},
    ],
}

# Cors configuration
CORS_ORIGIN_ALLOW_ALL = config("CORS_ORIGIN_ALLOW_ALL", cast=bool)
CORS_ALLOWED_ORIGINS = convert_csv_to_list(config("CORS_ALLOWED_ORIGINS", cast=str))
CORS_ALLOW_HEADERS = convert_csv_to_list(config("CORS_ALLOW_HEADERS", cast=str))
CORS_ALLOW_METHODS = convert_csv_to_list(config("CORS_ALLOW_METHODS", cast=str))
CORS_ALLOW_CREDENTIALS = config("CORS_ALLOW_CREDENTIALS", cast=bool)

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",  # Set drf-spectacular as the schema generator
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework_simplejwt.authentication.JWTAuthentication', ],
}

# JWT configuration
SIMPLE_JWT = {'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
              'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
              'ROTATE_REFRESH_TOKENS': True,
              'BLACKLIST_AFTER_ROTATION': True,
              'ALGORITHM': 'HS256',
              'SIGNING_KEY': SECRET_KEY,
              'VERIFYING_KEY': None,
              'AUTH_HEADER_TYPES': ('Bearer',),
              'USER_ID_FIELD': 'id',
              'USER_ID_CLAIM': 'user_id',
              'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
              'TOKEN_TYPE_CLAIM': 'token_type',
              }

# Email configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST", cast=str)
EMAIL_PORT = config("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", cast=str)
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str)
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", cast=str)

# Celery configuration
CELERY_BROKER_URL= config("CELERY_BROKER_URL", cast=str)
CELERY_ACCEPT_CONTENT=convert_csv_to_list(config("CELERY_ACCEPT_CONTENT", cast=str))
CELERY_TASK_SERIALIZER=config("CELERY_TASK_SERIALIZER", cast=str)
CELERY_RESULT_BACKEND= config("CELERY_RESULT_BACKEND", cast=str)
from datetime import timedelta


ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*', 'web:8000']

INSTALLED_APPS_DEV = [
    'django_extensions',
    'drf_yasg',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=14),
}

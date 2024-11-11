import os
import ssl
from pathlib import Path

from cryptography.fernet import Fernet

from .config import config

if not os.getenv("IS_TEST", False):
    from .logging_settings import LOGGING  # noqa: F401

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

fernet = Fernet(os.getenv("FERNET_KEY"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = fernet.decrypt(config.SECRET_KEY_ENCRYPTED.encode()).decode()

API_KEY = fernet.decrypt(config.API_KEY_ENCRYPTED.encode()).decode()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.DEBUG

ALLOWED_HOSTS = config.ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "drf_yasg",
    "rest_framework",
    "rest_framework.authtoken",
    "django_filters",
    "django_celery_beat",
    "src.validators",
    "src.accounts",
    "src.statistic",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "src.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB"),
        "USER": os.getenv("POSTGRES_USER"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
        "HOST": os.getenv("POSTGRES_HOST"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

CORS_ORIGIN_ALLOW_ALL = True

USE_X_FORWARDED_HOST = False

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "accounts.AdvUser"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/django-static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# DRF Settings
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# Always use PTPython for shell_plus
# https://django-extensions.readthedocs.io/en/latest/shell_plus.html#additional-imports
SHELL_PLUS = "ptpython"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# https://django-extensions.readthedocs.io/en/latest/shell_plus.html#additional-imports
SHELL_PLUS_IMPORTS = [
    "from src.utilities import RedisClient",
]

CELERY_BROKER_URL = f'rediss://:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}'

REDIS_CERTS_DIR = os.path.join(BASE_DIR, os.getenv("REDIS_CERTS_DIR"))

CELERY_BROKER_USE_SSL = {
    'ssl_cert_reqs': ssl.CERT_REQUIRED,
    'ssl_ca_certs': os.path.join(REDIS_CERTS_DIR, 'ca.crt'),
    'ssl_certfile': os.path.join(REDIS_CERTS_DIR, 'redis_server.crt'),
    'ssl_keyfile': os.path.join(REDIS_CERTS_DIR, 'redis_server.key'),
}
CELERY_REDIS_BACKEND_USE_SSL = CELERY_BROKER_USE_SSL


CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": f'rediss://:{os.getenv("REDIS_PASSWORD")}@{os.getenv("REDIS_HOST")}:{os.getenv("REDIS_PORT")}',
        "OPTIONS": {
            "ssl_cert_reqs": ssl.CERT_REQUIRED,
            "ssl_ca_certs": os.path.join(REDIS_CERTS_DIR, "ca.crt"),
            "ssl_certfile": os.path.join(REDIS_CERTS_DIR, "redis_server.crt"),
            "ssl_keyfile": os.path.join(REDIS_CERTS_DIR, "redis_server.key"),
        },
    }
}


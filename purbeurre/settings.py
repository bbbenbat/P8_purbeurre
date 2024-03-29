"""
Django settings for purbeurre project.
"""
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, default_value):
    try:
        return os.environ[var_name]
    except KeyError:
        if default_value is None:
            error_msg = "Configurer la variable d'environnement {}".format(
                var_name)
            raise ImproperlyConfigured(error_msg)
        else:
            return default_value


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'tjtkjyjypltplytumlb;ty54yj!hty478')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'researches.apps.OffAppConfig',  # new
    'django.contrib.sites',  # new
    'allauth',  # new
    'allauth.account',  # new
    'allauth.socialaccount',  # new
    'accounts',  # new
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'purbeurre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'purbeurre.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'p8purbeurre'),
        'USER': os.environ.get('DB_USER', 'p8purbeurreuser'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'Python2021'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # new
STATIC_URL = '/static/'  # new

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # new
MEDIA_URL = '/media/'  # new

AUTH_USER_MODEL = 'accounts.CustomUser'  # new

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1  # new

ACCOUNT_EMAIL_REQUIRED = True  # new
ACCOUNT_USERNAME_REQUIRED = False  # new
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False  # new
ACCOUNT_SESSION_REMEMBER = True  # new
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # new
ACCOUNT_UNIQUE_EMAIL = True  # new
ACCOUNT_LOGOUT_ON_GET = True  # new
LOGIN_REDIRECT_URL = 'home'  # new
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'  # new

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')  # new
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')  # new
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')  # new
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')  # new

AWS_S3_FILE_OVERWRITE = False  # new
AWS_DEFAULT_ACL = None  # new

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'  # new

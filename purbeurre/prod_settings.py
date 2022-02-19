import dj_database_url

from purbeurre.settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

ALLOWED_HOSTS = ['purbeurre8-ocr.herokuapp.com']



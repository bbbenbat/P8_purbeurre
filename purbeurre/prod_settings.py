import dj_database_url

from purbeurre.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

#DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

#ALLOWED_HOSTS = ['purbeurre-ocr.herokuapp.com']
ALLOWED_HOSTS = ['167.99.32.70']



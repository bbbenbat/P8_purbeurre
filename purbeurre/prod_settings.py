import dj_database_url

from purbeurre.settings import *

DEBUG = False
TEMPLATE_DEBUG = False

DATABASES['default'] = dj_database_url.config()

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

SECRET_KEY = '&6@7a)no4f^o(o3_2ta^)*5zu82p!^)guvu5v3b^1be+a)%(yw'

ALLOWED_HOSTS = ['purbeurre-ocr.herokuapp.com']



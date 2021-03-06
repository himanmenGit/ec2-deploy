from .base import *

DEBUG = True

secrets = json.loads(open(SECRETS_LOCAL, 'rt').read())
ALLOWED_HOSTS = []
DATABASES = secrets['DATABASES']

WSGI_APPLICATION = 'config.wsgi.local.application'

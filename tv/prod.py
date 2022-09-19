from .settings import *


DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ['https://*.herokuapp.com','https://*.127.0.0.1','https://unguocra.herokuapp.com']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd5amk8v9jdiugj',
        'USER': 'lhznimgisoodlh',
        'PASSWORD': 'a8c8597ce5aa83737736e5fc310d7bfe820bea7714ee429870fa251c23fa1c6a',
        'HOST': 'ec2-34-200-205-45.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

import django_heroku
django_heroku.settings(locals())
import os

from .common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yen5=v7%$s17dl5l3zumezo(m0g6a_c0b8yzr3b$&9p2khj%$!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
	'NAME': 'janus_dev',
        'USER': 'janus',
        'PASSWORD': 'janus',
        'HOST': '127.0.0.1',
        }
}

INTERNAL_IPS = ['192.168.56.1']

INSTALLED_APPS += (
    'autofixture',
)

STATICFILES_DIRS.append(
    os.path.join(BASE_DIR, os.pardir, 'frontend', 'build'),
)

CRONJOBS = [
    ('*/5 * * * *', 'backend.crons.update_controller_health')
]

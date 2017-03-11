# In production set the environment variable like this:
#    DJANGO_SETTINGS_MODULE=print_queue.settings.production
import logging.config

from .base import *  # NOQA

# For security and performance reasons, DEBUG is turned off
DEBUG = False
TEMPLATE_DEBUG = False

# Cache the templates in memory for speed-up
loaders = [
    ('django.template.loaders.cached.Loader', [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]),
]

TEMPLATES[0]['OPTIONS'].update({"loaders": loaders})
TEMPLATES[0].update({"APP_DIRS": False})

ADMINS = [('Aliaksei', 'aliaksei@aliakseipilko.com')]

ALLOWED_HOSTS = ['testbed.aliakseipilko.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-printcentral',
        'USER': 'printcentral',
        'PASSWORD': 'ATSUSwsQWQ4TQFmF',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
} 

# Define STATIC_ROOT for the collectstatic command
STATIC_ROOT = '/home/admin/web/testbed.aliakseipilko.com/django-apps/print_queue/static/'
STATIC_URL = "/3dprintcentral/static/"

MEDIA_ROOT = 'home/admin/web/testbed.aliakseipilko.com/django-apps/print_queue/media/'
MEDIA_URL = "/3dprintcentral/media/"

# Log everything to the logs directory at the top
LOGFILE_ROOT = join(dirname(BASE_DIR), 'logs')

# Reset logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'proj_log_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': join(LOGFILE_ROOT, 'project.log'),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'project': {
            'handlers': ['proj_log_file'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)

MIDDLEWARE_CLASSES += (
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
)

SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'


EMAIL_BACKEND = "mailer.backend.DbBackend"

EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = "3dprintcentral@testbed.aliakseipilko.com"
EMAIL_HOST_PASSWORD = "PnpSLxXzF8"
EMAIL_PORT = "25"
EMAIL_USE_TLS = True

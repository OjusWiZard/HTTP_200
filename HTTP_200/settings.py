"""
Django settings for HTTP_200 project.
Generated by 'django-admin startproject' using Django 1.8.2.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import HTTP_200.config_keys as config_keys
import config as config
from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.append(APPS_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'aq#*#1^qn$!_y04hrsg4!@ra5_!cn9v+39fzj=2rq^319s0^n6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

INTERNAL_IPS = '127.0.0.1'

APPEND_SLASH = True
# Application definition

INSTALLED_APPS = (
    'rest_framework',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'haystack',
    # 'feeds',
    'allauth',
    'allauth.account',
    'profiles',
    'notices',
    'autofixture',
    'ckeditor',
    'django_spaghetti',
    'debug_toolbar',
    'import_export',
    'wifi',
    'emailform',
    'rest_framework_docs',
    'rest_framework.authtoken',
    'notifications',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'HTTP_200.middlewares.SetLastVisitMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'HTTP_200.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, 'HTTP_200')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(TEMPLATE_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'profiles/templates'),
            # os.path.join(BASE_DIR, 'notices/templates'),
        ],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ]
        },
    },
]

WSGI_APPLICATION = 'HTTP_200.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.sqlite3',
#          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#      }
#  }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config_keys.DATABASE_NAME,
        'USER': config_keys.MYSQL_USERNAME,
        'PASSWORD': config_keys.MYSQL_PASSWORD,
        'HOST': config_keys.HOST,   # Or an IP Address that your DB is hosted on
        'PORT': config_keys.PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'auth.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 15,
}


CORS_ORIGIN_ALLOW_ALL = True

import datetime

JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
        'rest_framework_jwt.utils.jwt_encode_handler',

        'JWT_DECODE_HANDLER':
        'rest_framework_jwt.utils.jwt_decode_handler',

        'JWT_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_payload_handler',

        'JWT_PAYLOAD_GET_USER_ID_HANDLER':
        'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

        'JWT_RESPONSE_PAYLOAD_HANDLER':
        'rest_framework_jwt.utils.jwt_response_payload_handler',

        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_ALGORITHM': 'HS256',
        'JWT_VERIFY': True,
        'JWT_VERIFY_EXPIRATION': True,
        'JWT_LEEWAY': 0,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=360),
        'JWT_AUDIENCE': None,
        'JWT_ISSUER': None,

        'JWT_ALLOW_REFRESH': False,
        'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

        'JWT_AUTH_HEADER_PREFIX': 'JWT',
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# allauth settings
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_PASSWORD_MIN_LENGTH = 1

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(APP_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(TEMPLATE_DIR, 'static'),
)


LOGIN_REDIRECT_URL = reverse_lazy('relevent-notice-list')
SAMPLEDATAHELPER_SEED = 123456789


SAMPLEDATAHELPER_MODELS = [
    # Generate 5 instances completly random
    {'model': 'profiles.StudentDetail', 'number': 5, },

    # Generate 5 instances selecting random method for some fields
    {
        'model': 'profiles.StudentDetail',
        'number': 5,
        'fields_overwrite': [
            ('my_int_field', lambda _, sd: sd.int(5, 10)),
        ]
    },

    # Generate 5 instances with fixed data in a field
    {
        'model': 'profiles.StudentDetail',
        'number': 5,
        'fields_overwrite': [
            ('my_int_field', 5),
        ]
    }
]

MEDIA_ROOT = os.path.join(TEMPLATE_DIR, 'media')
MEDIA_URL = '/media/'

SPAGHETTI_SAUCE = {
    'apps': ['auth', 'notices', 'profiles', 'notifications'],
    'show_fields': True,
    # 'exclude':{'auth':['user']}
}

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'


EMAIL_HOST = config.HOST
EMAIL_HOST_USER = config.USERNAME
EMAIL_HOST_PASSWORD = config.PASSWORD
EMAIL_PORT = config.PORT
EMAIL_USE_TLS = config.TLS

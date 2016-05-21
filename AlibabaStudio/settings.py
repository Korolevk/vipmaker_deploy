# -*- coding:utf-8 -*-

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '...'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'alibaba',
    'loginsys',
    'pytz',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'AlibabaStudio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                # 'django.core.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'AlibabaStudio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '...',
        'USER': '...',
        'PASSWORD': '...',
        # 'HOST': '127.0.0.1',
        # 'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'GMT'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_FORMAT = 'd.m.Y'           # 18.09.2009
DATETIME_FORMAT = 'd.m.Y H:i'   # 18.09.2009 22:41
TIME_FORMAT = 'H:i'


EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = "op.96@mail.ru"
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = 'tmp/messages/'

# MEDIA_ROOT_DIR = 'uploads'
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
# MEDIA_ROOT = "/home/kirill/Рабочий стол/vipmaker/uploads/"



PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'alibaba/static'),
)

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

try:
    from AlibabaStudio.local_settings import *
except ImportError:
    print("No local file in my project (look into file local_settings.py.skeleton)")
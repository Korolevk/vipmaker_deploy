
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0mgys*rp#qgel!@--h4tqxg52lr)9l5n=c7y3j3f)hv*b@rmc#'

# SECURITY WARNING: don't run with debug turned on in production!
# False in production
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'db.sqlite3',
#     }
# }

# mysql://bf57ad98c2deef:2ccec42e@eu-cdbr-west-01.cleardb.com/heroku_1b569c743f60ace?reconnect=true

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_1b569c743f60ace',
        'USER': 'bf57ad98c2deef',
        'PASSWORD': '2ccec42e',
        'HOST': 'eu-cdbr-west-01.cleardb.com',
        # 'PORT': '3306',
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

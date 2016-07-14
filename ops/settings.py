"""
Django settings for ops project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9f56ob(g*e(lankg6vj%c3%hb@j@eveib#7(%@yed2*9ux0_c$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'xadmin',
    'crispy_forms',
    'reversion',

    'cmdb',
    'deploy',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ops.urls'

WSGI_APPLICATION = 'ops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        #'ENGINE': 'mysql.connector.django',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ops',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR,'static/')

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'

SITE_ID = 1



MY_IGNORED_WARNINGS = {
    'RemovedInDjango18Warning: `PublisherManager.get_query_set`',
    'RemovedInDjango18Warning: `PageManager.get_query_set`',
    'RemovedInDjango18Warning: `CMSChangeList.get_query_set`',
    'form PagePermissionInlineAdminForm needs updating',
    'form ViewRestrictionInlineAdminForm needs updating',
    'form PageUserForm needs updating',
    '/xadmin/views/form_view.py:129: RemovedInDjango18Warning: commit_on_success is deprecated in favor of atomic.',
    'RemovedInDjango18Warning: `PagePermissionInlineAdmin.queryset',
    'RemovedInDjango18Warning: `ViewRestrictionInlineAdmin.queryset`',
    'RemovedInDjango18Warning: `PageUserAdmin.queryset`',

}

def filter_djangocms_warnings(record):
    for ignored in MY_IGNORED_WARNINGS:
        if ignored in record.args[0]:
            return False
    return True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'filters': {
        'ignore_djangocms_warnings': {
            '()': 'django.utils.log.CallbackFilter',
            'callback': filter_djangocms_warnings,
        },
    },
    'loggers': {
        'py.warnings': {
            'handlers': ['console', ],
            'filters': ['ignore_djangocms_warnings', ],
        }
    },
}

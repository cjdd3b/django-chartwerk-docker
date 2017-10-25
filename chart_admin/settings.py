"""
Settings for chart_admin project.
"""

import os

PROJECT_NAME = 'chart_admin'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, PROJECT_NAME)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*g1f$7=sufb4!#(7mdlm7$!+1i+w51&!86+sv9xz2w5zbs$pdo'

ALLOWED_HOSTS = ['*']

DEBUG = False


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'chartwerk',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'chart_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./chart_admin/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'chart_admin.wsgi.application'


# Database. Set using environment variables in config/env
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'postgres'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images). Set in environment variables.
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = os.getenv('STATIC_URL', '/static/')
STATIC_ROOT= os.getenv('STATIC_ROOT', '/static/')


# Chartwerk. Gibberish in local dev, but use environment variables to connect to S3 in prod.

CHARTWERK_DOMAIN = os.getenv('CHARTWERK_DOMAIN', 'https://yourapp.com')
CHARTWERK_AWS_BUCKET = os.getenv('CHARTWERK_AWS_BUCKET', 'chartwerk')
CHARTWERK_AWS_ACCESS_KEY_ID = os.getenv('CHARTWERK_AWS_ACCESS_KEY_ID', 'YOUR_ACCESS_KEY')
CHARTWERK_AWS_SECRET_ACCESS_KEY = os.getenv('CHARTWERK_AWS_SECRET_ACCESS_KEY', 'YOUR_SECRET_KEY')


# Celery. Connects to containerized Redis, but could change these for hosted Redis.
# https://github.com/pahaz/docker-compose-django-postgresql-redis-example/blob/master/sources/_project_/settings.py

REDIS_HOST = 'redis'
CELERY_BROKER_URL = 'redis://%s:6379/0' % REDIS_HOST
CELERY_RESULT_BACKEND = 'redis://%s:6379/0' % REDIS_HOST
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
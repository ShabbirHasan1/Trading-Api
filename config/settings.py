"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 3.2.9.
For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import datetime
import os
from pathlib import Path

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

# import django
# django.setup()
#
# from django.core.management import call_command
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o_63(=jef-u98!)t**=wm)68$g!6_^-xy29l)=v$53rkrd37q7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',

    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'dj_rest_auth.registration',

    # Cross Headers
    'corsheaders',

    # 'django.contrib.contenttypes.apps.AppConfig',
]

MIDDLEWARE = [
    # Cross Header
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


]

# Allow Access To All Cross Header
CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'
# ASGI_APPLICATION = "config.routing.application"

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }
####################################################################################################
# mammads redis
import ssl

ssl_context = ssl.SSLContext()
ssl_context.check_hostname = False

heroku_redis_ssl_host = {
    # 'address': 'redis://:p55213883d08c65b47a0167580163fa148ac5fd73f09b32d14e22af68c4463b67@ec2-3-210-19-106.compute-1.amazonaws.com:18010',  # The 'rediss' schema denotes a SSL connection.
    'address': 'redis://:p55213883d08c65b47a0167580163fa148ac5fd73f09b32d14e22af68c4463b67@ec2-52-204-98-153.compute-1.amazonaws.com:28160',  # The 'rediss' schema denotes a SSL connection.
    'ssl': ssl_context

}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': (heroku_redis_ssl_host,)
        }
    },
}
#################################################################################################################
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dch0f5uef62aoc',
#         'USER': 'mngoilajihazhg',
#         'PASSWORD': 'd1b536269ee7a9b3dd15e180f5862c09029e75a4f043d119ea9f14ec6247bc75',
#         'HOST': 'ec2-54-147-203-50.compute-1.amazonaws.com',
#         'PORT': '5432'
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd49noiaur1s5kc',
#         'USER': 'lqdqkbcqmgbdhv',
#         'PASSWORD': '4d9af77fa1728e3372efab0e5b5368a3fc5bdbd44ced1add7e994cd31c9c8232',
#         'HOST': 'ec2-3-227-15-75.compute-1.amazonaws.com',
#         'PORT': '5432'
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd11aj9ec8sae3d',
#         'USER': 'xamdizcyolyctj',
#         'PASSWORD': 'a92d8e8dcd4682ffee09491fa04c3f3e944268fa447e8f18a0465dd69e0b997f',
#         'HOST': 'ec2-54-146-73-98.compute-1.amazonaws.com',
#         'PORT': '5432'
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

from datetime import timedelta

SIMPLE_JWT = {
     'ACCESS_TOKEN_LIFETIME': timedelta(weeks=2),
     'REFRESH_TOKEN_LIFETIME': timedelta(weeks=5),

}

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/templates/'

# location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR, 'templates')

# location where you will store your static files
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'api/templates')]

# White Noise Storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'api.permissions.IsStaffOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    )

}

SITE_ID = 1
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'access'
JWT_AUTH_REFRESH_COOKIE = 'refresh'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10240 # higher than the count of fields

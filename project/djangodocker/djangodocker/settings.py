from .version import info
from datetime import timedelta
from pathlib import Path

import environ
import os
import random


URIPATH = Path(os.path.dirname(__file__)).joinpath(".env")
env = environ.Env(DEBUG=(bool,False))
environ.Env.read_env(env_file=str(URIPATH))

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY')

JWT_KEY = ''.join(random.sample(SECRET_KEY, len(SECRET_KEY)))

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['*']

AUTH_APPS = [
#     'rest_auth',
    # 'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'rest_auth.registration',
]

CUSTOM_APPS = [
    'apps.core',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DJANGOREST_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'rest_registration',
]

REST_USE_JWT = True

    # 'rest_auth',
    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'rest_auth.registration',
    # 'corsheaders',

INSTALLED_APPS = DJANGO_APPS + DJANGOREST_APPS + AUTH_APPS + CUSTOM_APPS

# SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',
    ),
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated', 
    # ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=90),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=365),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': JWT_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('NOUVE',), # Replace 'Bearer'. (NOUVE)
    'AUTH_HEADER_NAME': 'HTTP_X_NOUVE_TOKEN', # Replace 'Authorization'. (X-NOUVE-TOKEN)
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=90),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=365),
}

REST_REGISTRATION = {
    'REGISTER_VERIFICATION_ENABLED': False,
    'REGISTER_EMAIL_VERIFICATION_ENABLED': False,
    'RESET_PASSWORD_VERIFICATION_ENABLED': False,
}

# REST_REGISTRATION = {
#     'REGISTER_VERIFICATION_ENABLED': True,
#     'RESET_PASSWORD_VERIFICATION_ENABLED': True,
#     # 'REGISTER_EMAIL_VERIFICATION_ENABLED': False,    
#     'REGISTER_VERIFICATION_URL': 'http://127.0.0.1:8000/api/accounts/verify-registration/',
#     'RESET_PASSWORD_VERIFICATION_URL': 'http://127.0.0.1:8000/api/accounts/reset-password/',
#     'REGISTER_EMAIL_VERIFICATION_URL': 'http://127.0.0.1:8000/verify-email/',
#     'VERIFICATION_FROM_EMAIL': 'no-reply@example.com',
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangodocker.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'djangodocker.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
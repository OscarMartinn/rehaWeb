"""
Django settings for rehaWeb project.

Generated by 'django-admin startproject' using Django 1.11.29.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!l%l6n#*(eny7gy2-+m-(o*dzacscw2l01i+=u14&0w&bm@$5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
workingOnServer = False

ALLOWED_HOSTS = ['*','13.37.112.81']

#PREPEND_WWW = True
#BASE_URL = "https://www.rehabot.xyz"

#CSRF_COOKIE_HTTPONLY = True
#CSRF_COOKIE_SECURE = True
#SECURE_HSTS_SECONDS = 3600
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_SSL_REDIRECT = True # Con el certificado SSL poner a true
#SECURE_HSTS_PRELOAD = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rehaWebApp',
    'accesoTerapeutas',
    'englishAccess',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rehaWeb.urls'

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

WSGI_APPLICATION = 'rehaWeb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
#DATABASES = {
#        'default': {
#                'ENGINE':'django.db.backends.mysql',
#                'OPTIONS': {
#                        'read_default_file':'/home/ubuntu/Web/auth/mysql.cnf',
#                },
#        }
#}



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

LANGUAGE_CODE = 'es-eu'
LANGUAGES = [
    ('es','Spanish'),
    ('en','English'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR,'locale')
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/Web/site/public/static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media/')





DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## Configuración para GMAIL
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = "smtp.gmail.com"
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = "omartincas@gmail.com"
#EMAIL_HOST_PASSWORD = "cangog-1nycga-tyswIx"

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_HOST_USER = 'rehaweb@outlook.es'
EMAIL_HOST_PASSWORD = 'fuMvvh-r23$?a'
EMAIL_PORT = 587



LOGIN_REDIRECT_URL = '/accesoTerapeutas/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

DATE_INPUT_FORMATS = ['%d-%m-%Y']

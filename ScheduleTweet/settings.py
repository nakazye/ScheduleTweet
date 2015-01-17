"""
Django settings for ScheduleTweet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
hostname = socket.gethostname()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'staticfiles'), )

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(g9&(6=cijx5pdqb30*kch2rwdwf6fqix=5$t4fsba@&d6+u29'

# SECURITY WARNING: don't run with debug turned on in production!
if 'local' in hostname:
    DEBUG = True
    TEMPLATE_DEBUG = True
else:
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['*']

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # social-auth
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_TWITTER_KEY = 'zbJ98ZCTitjdTDtf6Y0wjFA6j'
SOCIAL_AUTH_TWITTER_SECRET = 'BSZn8c349GJ8dpcpghAdjaU8UzD49NtUfwsX6knm1X5M2YCr6b'
SOCIAL_AUTH_TWITTER_KEY_FOR_POST = '8Ar71vacawVAr9PpXFNXIM9kI'
SOCIAL_AUTH_TWITTER_SECRET_FOR_POST = 'SlUBGJnZr2sHVPSbadzDl6g8H8go2FGkWy0XZwLNX2XWPKQVys'
SOCIAL_AUTH_TWITTER_ACCESS_FOR_POST = '2985452046-AwydKTBrgiq8isdFkxbpHolAxgaPirmH94o9taY'
SOCIAL_AUTH_TWITTER_ACCESS_SECRET_FOR_POST = '6bPGB52sdhFYY276bby6TW54L4h7BxCDTxTy5acc58YA8'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'ScheduleTweet',
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

ROOT_URLCONF = 'ScheduleTweet.urls'

WSGI_APPLICATION = 'ScheduleTweet.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
if 'local' in hostname:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config()
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


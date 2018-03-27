"""
Django settings for hikkiBlog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g_2)gzw3ljl!=7*^6pv#st($d)3=^=zcesgi*$%eo1@7ze85^5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['myhikki.com','www.myhikki.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taggit',
    'blog',
    'disqus',
    'tinymce',
    'sorl.thumbnail',
    'django.contrib.staticfiles',
    'blog.templatetags.inline_thumbnails',
    
)

DISQUS_WEBSITE_SHORTNAME = 'myhikkicomblog'
DISQUS_API_KEY = "bv0mcJMw17ws9MuEHScaR4OUvQRagRIZHRBBYjNatOiiEm9OFaPpb2mEEU6FRFZl"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hikkiBlog.urls'

WSGI_APPLICATION = 'hikkiBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'blog',
        'USER': 'd',
        'PASSWORD': 'ex,
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS= (
    '/var/www/django/static/templates/',
    )
FILE_UPLOAD_PERMISSIONS = 0644
if not DEBUG:
    MEDIA_URL = '/media/'
    STATIC_ROOT = '/var/www/static/'
    MEDIA_ROOT =  '/var/www/static/media/'
    STATICFILES_DIRS = (
        '/var/www/static/static/',
    )

    TEMPLATE_DIRS= (
    '/var/www/static/templates/',
    )

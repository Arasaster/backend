"""
Django settings for ifeolowu project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY environment variable is missing!")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

PAYSTACK_SECRET_KEY = 'sk_test_684afab632c8b071a9ae3de5b417a3cb918e67d5'
PAYSTACK_PUBLIC_KEY = 'pk_test_fec286b46a2c2a258d57df221df4ce9289562b5e'

ALLOWED_HOSTS = [
    '*',
]

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'shop',
    'blog',
    'newsletter',
    'core',
]

# Middleware settings
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ifeolowu.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Keep this empty if you're using APP_DIRS
        'APP_DIRS': True,  # This must be True to search inside app folders
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

WSGI_APPLICATION = 'ifeolowu.wsgi.application'

# ✅ Force SQLite3 Usage - Ignore Render DATABASE_URL
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}

SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1 localhost ifeolowu.com").split()


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC files (e.g. CSS, JS, site images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # For manually placed static files
STATIC_ROOT = BASE_DIR / "staticfiles"    # Where collectstatic copies everything

# MEDIA files (e.g. user uploads like images/videos)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Django messages framework
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {messages.ERROR: 'danger'}

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8000',
    'https://localhost:8000',
]

# Remita Configuration
REMITA_PUBLIC_KEY = 'KLTILUKE8JFUITR2'
REMITA_SECRET_KEY = 'H8UJKGPI1ALHL20E98PWEP04V5KXHS1M'
REMITA_MERCHANT_ID = '27768931'
REMITA_API_URL = 'https://remitademo.net/payment/v1/payment/initialize'  # Test environment
# REMITA_API_URL = 'https://login.remita.net/payment/v1/payment/initialize'  # Production environment
REMITA_VERIFY_URL = 'https://remitademo.net/payment/v1/payment/'  # Test environment
# REMITA_VERIFY_URL = 'https://login.remita.net/payment/v1/payment/'  # Production environment


# Merchant ID: 2547916
# API Key: 1946
# Service Type ID: 4430731
# Recurring payments
# Merchant ID: 27768931
# Service Type ID: 35126630
# API Key: Q1dHREVNTzEyMzR8Q1dHREVNTw==
# API Token: SGlQekNzMEdMbjhlRUZsUzJCWk5saDB6SU14Zk15djR4WmkxaUpDTll6bGIxRCs4UkVvaGhnPT0=
# Funds Transfer (Bulk)
# Public Key: KLTILUKE8JFUITR2
# Secret Key: H8UJKGPI1ALHL20E98PWEP04V5KXHS1M
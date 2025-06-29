from pathlib import Path
import os
from decouple import config
import sys
import sentry_sdk


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

HOST_URL = config("HOST_URL")

ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]", "0.0.0.0","1.1.1.1","8080",
                     HOST_URL,"www.crea-therapy.com","crea-therapy.com"]

CSRF_TRUSTED_ORIGINS = [
     "https://"+HOST_URL,
     "https://www.crea-therapy.com",
     "https://crea-therapy.com"
]

# Application definition

INSTALLED_APPS = [
    #* My apps
    'between_app',
    'learning_logs',
    'accounts.apps.AccountsConfig',
    'techniques_app',
    'dive_app',

    #* Third party apps
    'django_bootstrap5', #css framework
    "django_browser_reload", # for automatic reload after save


    'allauth',
    'allauth.account', #authorisations
    #'allauth.socialaccount', #the social account sytem 
    #'allauth.socialaccount.providers.apple', #apple social account
    #'allauth.socialaccount.providers.google', #google social account
    'allauth.mfa',
    "django.contrib.humanize",


    "whitenoise.runserver_nostatic", #white noise, static files manager

    #* Django apps added
    'django.contrib.flatpages', #for flat pages
    'django.contrib.sites',
    'django.contrib.sitemaps', # sitemaps

    #* Defoult apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', #for statics

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware", #static files manager
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware', #allauth middleware
    "django_browser_reload.middleware.BrowserReloadMiddleware", # reload middleware

]

ROOT_URLCONF = 'between.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
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

WSGI_APPLICATION = 'between.wsgi.application'


# for the virtual machine to take over in global variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRESS_NAME'),
        'USER': config('POSTGRESS_USER'),
        'PASSWORD': config('POSTGRESS_KEY'),
        'HOST': config('POSTGRESS_HOST'),
        'PORT': config('POSTGRESS_PORT'),
    }
}

# moving to a cache in the database
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = "static/" #change when knowing the reall address, plus change url patterns
MEDIA_URL = 'media/'

STORAGES = {
    # Enable WhiteNoise's GZip and Brotli compression of static assets:
    # https://whitenoise.readthedocs.io/en/latest/django.html#add-compression-and-caching-support
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Don't store the original (un-hashed filename) version of static files, to reduce slug size:
# https://whitenoise.readthedocs.io/en/latest/django.html#WHITENOISE_KEEP_ONLY_HASHED_FILES
WHITENOISE_KEEP_ONLY_HASHED_FILES = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# My settings

LOGIN_REDIRECT_URL = 'between_app:index'
LOGOUT_REDIRECT_URL = 'between_app:index'
LOGIN_URL = 'account_login'
AUTHENTICATION_LOGOUT_REDIRECT = 'between_app:index'
AUTH_USER_MODEL = 'accounts.CustomUser'
ACCOUNT_LOGIN_BY_CODE_ENABLED = True

MFA_TOTP_ISSUER = 'Crea-Therapy'

MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True


#config of bootstrap5, I added a theme called 'sandstone' from bootswatch
BOOTSTRAP5 = {

    # The complete URL to the Bootstrap CSS file.
    # Note that a URL can be either a string
    # ("https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css"),
    # or a dict with keys `url`, `integrity` and `crossorigin` like the default value below.
    "css_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/css/bootstrap.min.css",
        "integrity": "sha384-SgOJa3DmI69IUzQ2PVdRZhwQ+dy64/BUtbMJw1MZ8t5HZApcHrRKUc4W0kG879m7",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap bundle JavaScript file.
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.5/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-k6d4wzSIapyDyv1kpU366/PK5hCdSbCRGRCMv+eplOQJWyd1fbcAu9OCUj5zNLiq",
        "crossorigin": "anonymous",
    },

    # The complete URL to the Bootstrap CSS theme file (None means no theme).
    "theme_url": "https://bootswatch.com/5/sandstone/bootstrap.css",
}

#REsend configuration and email back ends
RESEND_API_KEY = config('RESEND_API_KEY')
RESEND_SMTP_PORT = 587
RESEND_SMTP_USERNAME = 'resend'
RESEND_SMTP_HOST = 'smtp.resend.com'

#resend activated all the time
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = RESEND_SMTP_HOST
EMAIL_USE_TLS = True
EMAIL_PORT = RESEND_SMTP_PORT
EMAIL_USE_SSL = False
EMAIL_HOST_USER = RESEND_SMTP_USERNAME
EMAIL_HOST_PASSWORD = RESEND_API_KEY
DEFAULT_FROM_EMAIL = 'gabriel@crea-therapy.com'


#* Django All auth config
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_FORM_HONEYPOT_FIELD = 'phone_number'

ACCOUNT_FORMS = {'signup': 'accounts.forms.MyCustomSignupForm',
                 'login': 'accounts.forms.MyCustomLoginForm'}

#* Debug Tool bar

TESTING = "test" in sys.argv

if not TESTING and DEBUG:
    MFA_WEBAUTHN_ALLOW_INSECURE_ORIGIN = True # passkey for local development allauth

    INSTALLED_APPS = [
        *INSTALLED_APPS,
        "debug_toolbar",
    ]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *MIDDLEWARE,
    ]

INTERNAL_IPS = [
    "127.0.0.1",
]

#* Sentry
if not DEBUG:
    sentry_sdk.init(
        dsn=config('SENTRY_DSN'),
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for tracing.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )


# logging conf to add some info when things are wrong (there are more complex setups). 
# By default django messages are shown when debug True even in info level.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "WARNING",
    },
}
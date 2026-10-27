from pathlib import Path

import sentry_sdk
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)
TEMPLATE_DEBUG = DEBUG

HOST_URL = config("HOST_URL")

ALLOWED_HOSTS = [
    ".localhost",
    "127.0.0.1",
    "[::1]",
    "0.0.0.0",
    "1.1.1.1",
    "8080",
    "8000",
    "3000",
    HOST_URL,
    "www.crea-therapy.com",
    "crea-therapy.com",
]

CSRF_TRUSTED_ORIGINS = ["https://" + HOST_URL, "https://www.crea-therapy.com", "https://crea-therapy.com"]

# Application definition

INSTALLED_APPS = [
    # * My apps
    "between_app",
    "learning_logs",
    "accounts.apps.AccountsConfig",
    "techniques_app",
    "dive_app",
    "cards_app",
    "companion_app",
    # * Third party apps
    "orbit",
    "django_bootstrap5",  # css framework
    "django_browser_reload",  # for automatic reload after save
    "django_htmx",
    "allauth",
    "allauth.account",  # authorisations
    "allauth.mfa",
    "django.contrib.humanize",
    "whitenoise.runserver_nostatic",  # white noise, static files manager
    # * Django apps added
    "django.contrib.flatpages",  # for flat pages
    "django.contrib.sites",
    "django.contrib.sitemaps",  # sitemaps
    # * Defoult apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",  # for statics
]

MIDDLEWARE = [
    "orbit.middleware.OrbitMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files manager
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # allauth middleware
    "django_browser_reload.middleware.BrowserReloadMiddleware",  # reload middleware
    "django_htmx.middleware.HtmxMiddleware",  # django htmx
    "between.middleware.SubdomainMiddleware",  # subdomain middleware by Me
]

ROOT_URLCONF = "between.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "between/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # "between.context_processors.dynamic_base",  # my context processor to change the base template by subdomain
            ],
        },
    },
]

WSGI_APPLICATION = "between.wsgi.application"


# for the virtual machine to take over in global variables
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRESS_NAME"),
        "USER": config("POSTGRESS_USER"),
        "PASSWORD": config("POSTGRESS_KEY"),
        "HOST": config("POSTGRESS_HOST"),
        "PORT": config("POSTGRESS_PORT"),
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
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/London"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / "between/staticfiles"]
STATIC_URL = "static/"
STATIC_ROOT = "assets/"  # change when knowing the reall address, plus change url patterns
MEDIA_URL = "media/"

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# My settings

LOGIN_REDIRECT_URL = "base_app:index"
LOGOUT_REDIRECT_URL = "base_app:index"
LOGIN_URL = "account_login"
AUTHENTICATION_LOGOUT_REDIRECT = "base_app:index"
AUTH_USER_MODEL = "accounts.CustomUser"
ACCOUNT_LOGIN_BY_CODE_ENABLED = True

MFA_TOTP_ISSUER = "Crea-Therapy"

MFA_SUPPORTED_TYPES = ["totp", "webauthn", "recovery_codes"]
MFA_PASSKEY_LOGIN_ENABLED = True


# config of bootstrap5, I added a theme called 'sandstone' from bootswatch
BOOTSTRAP5 = {
    "javascript_url": {
        "url": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js",
        "integrity": "sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI",
        "crossorigin": "anonymous",
    },
}

# REsend configuration and email back ends
RESEND_API_KEY = config("RESEND_API_KEY")
RESEND_SMTP_PORT = 587
RESEND_SMTP_USERNAME = "resend"
RESEND_SMTP_HOST = "smtp.resend.com"

# resend activated all the time
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = RESEND_SMTP_HOST
EMAIL_USE_TLS = True
EMAIL_PORT = RESEND_SMTP_PORT
EMAIL_USE_SSL = False
EMAIL_HOST_USER = RESEND_SMTP_USERNAME
EMAIL_HOST_PASSWORD = RESEND_API_KEY
DEFAULT_FROM_EMAIL = "gabriel@crea-therapy.com"


# * Django All auth config
SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]

ACCOUNT_SIGNUP_FORM_HONEYPOT_FIELD = "phone_number"

ACCOUNT_FORMS = {"signup": "accounts.forms.MyCustomSignupForm", "login": "accounts.forms.MyCustomLoginForm"}

ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = False


INTERNAL_IPS = [
    "127.0.0.1",
]

# * Sentry
if not DEBUG:
    sentry_sdk.init(
        dsn=config("SENTRY_DSN"),
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

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_SECONDS = 300


# settings.py

ORBIT_CONFIG = {
    # Core Settings
    "ENABLED": True,
    "AUTH_CHECK": lambda request: request.user.is_staff,
    # Callable or path to function
    "STORAGE_LIMIT": 1000,
    # Recording Settings - Phase 1 (Core)
    "RECORD_REQUESTS": True,
    "RECORD_QUERIES": True,
    "RECORD_LOGS": True,
    "RECORD_EXCEPTIONS": True,
    "RECORD_DUMPS": True,
    # Recording Settings - Phase 2 (Extended)
    "RECORD_COMMANDS": True,
    "RECORD_CACHE": True,
    "RECORD_MODELS": True,
    "RECORD_HTTP_CLIENT": True,
    "RECORD_MAIL": True,
    "RECORD_SIGNALS": False,
    # Recording Settings - Phase 3 (v0.5.0)
    "RECORD_JOBS": False,  # Background jobs (Celery, Django-Q, RQ, APScheduler)
    "RECORD_REDIS": False,  # Redis operations
    "RECORD_GATES": False,  # Permission/Gate checks
    # Recording Settings - Phase 4 (v0.6.0)
    "RECORD_TRANSACTIONS": True,  # Database transaction blocks
    "RECORD_STORAGE": True,  # File storage operations
    # AI/LLM Watcher (v0.12.0+)
    "RECORD_LLM": True,
    "LLM_CAPTURE_CONTENT": False,
    "LLM_CAPTURE_TOOL_CALL_ARGUMENTS": False,
    "LLM_MAX_CONTENT_CHARS": 2000,
    # MCP Server (v0.7.0+)
    "MCP_ENABLED": False,
    "MCP_INCLUDE_PAYLOADS": False,
    "MCP_MAX_LIMIT": 100,
    "MCP_MAX_PAYLOAD_CHARS": 12000,
    # Storage Backend (v0.8.0+)
    "STORAGE_BACKEND": "orbit.backends.database.DatabaseBackend",
    "STORAGE_DB_ALIAS": "orbit",  # only used by DjangoDBBackend
    # Query recording (v0.8.1+)
    "BULK_CREATE_BATCH_SIZE": None,  # set to e.g. 500 to avoid MySQL max_allowed_packet errors
    # Resilience
    "WATCHER_FAIL_SILENTLY": True,  # failed watchers log errors but don't crash
    # Performance Settings
    "SLOW_QUERY_THRESHOLD_MS": 500,
    # Path Filtering
    "IGNORE_PATHS": [
        "/orbit/",
        "/static/",
        "/media/",
        "/admin/jsi18n/",
        "/favicon.ico",
    ],
    # Security Settings
    "HIDE_REQUEST_HEADERS": [
        "Authorization",
        "Cookie",
        "X-CSRFToken",
    ],
    "HIDE_REQUEST_BODY_KEYS": [
        "password",
        "token",
        "secret",
        "api_key",
        "apikey",
        "access_token",
        "refresh_token",
    ],
    "MAX_BODY_SIZE": 65536,
}

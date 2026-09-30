"""
Django settings for smartcanteen project.
"""

from pathlib import Path
import os

# PyMySQL is a pure-Python MySQL driver: no C compiler or system
# libraries needed, so it installs cleanly on any host (Render etc.).
import pymysql

pymysql.version_info = (2, 2, 1, "final", 0)  # satisfy Django's version check
pymysql.install_as_MySQLdb()


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-local-development-key-change-in-production"
)

DEBUG = os.environ.get("DEBUG", "True").lower() == "true"


# =========================================================
# ALLOWED HOSTS
# =========================================================

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "testserver",
    ".onrender.com",
    ".vercel.app",
]


# Additional hosts from environment variable
extra_hosts = os.environ.get("ALLOWED_HOSTS")

if extra_hosts:
    ALLOWED_HOSTS.extend(
        [
            host.strip()
            for host in extra_hosts.split(",")
            if host.strip()
        ]
    )


# Render hostname
render_host = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if render_host and render_host not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(render_host)


# =========================================================
# CSRF TRUSTED ORIGINS
# =========================================================

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]


# Render CSRF origin
if render_host:
    CSRF_TRUSTED_ORIGINS.append(
        f"https://{render_host}"
    )


# Additional CSRF origins from environment variable
extra_csrf = os.environ.get("CSRF_TRUSTED_ORIGINS")

if extra_csrf:
    CSRF_TRUSTED_ORIGINS.extend(
        [
            origin.strip()
            for origin in extra_csrf.split(",")
            if origin.strip()
        ]
    )


# Render terminates HTTPS at its proxy; trust its header
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "canteen",
]


# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # WhiteNoise for static files
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# =========================================================
# URL CONFIGURATION
# =========================================================

ROOT_URLCONF = "smartcanteen.urls"


# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [
            BASE_DIR / "templates",
        ],

        "APP_DIRS": True,

        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# =========================================================
# WSGI
# =========================================================

WSGI_APPLICATION = "smartcanteen.wsgi.application"


# =========================================================
# DATABASE - AIVEN MYSQL
# =========================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",

        "NAME": os.environ.get(
            "MYSQL_DATABASE",
            "defaultdb"
        ),

        "USER": os.environ.get(
            "MYSQL_USER",
            "avnadmin"
        ),

        "PASSWORD": os.environ.get(
            "MYSQL_PASSWORD",
            ""
        ),

        "HOST": os.environ.get(
            "MYSQL_HOST",
            "smartcanteen-db-divya120107-7abd.d.aivencloud.com"
        ),

        "PORT": os.environ.get(
            "MYSQL_PORT",
            "26554"
        ),

        "OPTIONS": {
            # Encrypted connection (Aiven requires SSL)
            "ssl": {"check_hostname": False},
            "charset": "utf8mb4",
        },

        "CONN_MAX_AGE": 600,

        "CONN_HEALTH_CHECKS": True,
    }
}


# =========================================================
# PASSWORD VALIDATION
# =========================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# =========================================================
# LANGUAGE AND TIME ZONE
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True


# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Django 5.1+ removed STATICFILES_STORAGE; STORAGES is the new setting.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# =========================================================
# MEDIA / FOOD IMAGES
# =========================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"


# =========================================================
# EMAIL
# =========================================================

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)


# =========================================================
# DEFAULT PRIMARY KEY
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# =========================================================
# AUTHENTICATION REDIRECTS
# =========================================================

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "admin_orders"

LOGOUT_REDIRECT_URL = "home"
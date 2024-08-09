"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates/"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-zmysqq4f6r!!va5m5vh%vw5=8(gn4xy7250po7=$n4*)%n*0is"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',

    'CookingStories',
    
    "django_htmx",
    'allauth',
    'allauth.account',
    'widget_tweaks',
    'ckeditor',
    'ckeditor_uploader',

    # Optional -- requires install using `django-allauth[socialaccount]`.
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',




]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        'DIRS': [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",

            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',

]

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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

LANGUAGE_CODE = 'en-us'  # Yeh setting batati hai ki default language English (US) hogi.

TIME_ZONE = 'Asia/Kolkata'  # Yeh setting batati hai ki default time zone Asia/Kolkata hogi.

TIME_ZONE = 'UTC'  # Yeh setting batati hai ki default time zone UTC hogi. (Aapka pehla Time Zone overwrite ho gaya.)

USE_I18N = True  # Yeh setting enable karti hai internationalization ko, taaki aapki app multiple languages support kar sake.

USE_TZ = True  # Yeh setting enable karti hai time zone awareness ko. Django timezone-aware dates aur times ko handle karega.

STATICFILES_DIRS = [BASE_DIR.joinpath("staticfiles")]  # Yeh setting Django ko batati hai ki additional static files directory "staticfiles" mein milegi.

STATIC_ROOT = BASE_DIR.joinpath("static")  # Yeh setting batati hai ki collectstatic command se sab static files kahan collect hongi, yani "static" folder mein.

MEDIA_URL = "media/"  # Yeh URL prefix hai media files ke liye. Jab aap media files ko serve karte ho, yeh URL prefix use hoga.

MEDIA_ROOT = BASE_DIR.joinpath("media")  # Yeh setting batati hai ki uploaded media files "media" directory mein store hongi.

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Yeh setting define karti hai default field type for primary key auto fields in Django models.

LOGIN_REDIRECT_URL = "home"  # Yeh URL hai jahan user ko login ke baad redirect kiya jayega. (Is case mein home page.)

LOGOUT_REDIRECT_URL = "login"  # Yeh URL hai jahan user ko logout ke baad redirect kiya jayega. (Is case mein login page.)

LOGIN_URL = "login"  # Yeh URL hai jahan user ko redirect kiya jayega jab wo login page access karega.

CKEDITOR_UPLOAD_PATH = "uploads/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SITE_ID = 1 

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            'profile',
            'email',
        ],
        "AUTH_PARAMS":{
            "access_type": "online",
        }
    },
}

    # 'facebook': {
    #     'SCOPE': [
    #         'email',
    #         'public_profile',
    #     ],
    #     'AUTH_PARAMS': {
    #         'auth_type': 'online',
    #     },
    # }

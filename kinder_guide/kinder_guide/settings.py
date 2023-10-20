from pathlib import Path
from datetime import timedelta
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-yir#vh&^tzfltm4qd=1*wp6@4()41%n0*mz2edk0b7g6f(q_kb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# IF TRUE - USES SQLITE3 FOR LOCAL TASTING, IF FALSE - USES POSTGRESQL
LOCAL_DB = False

LOCAL_EMAIL = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'kinder.acceleratorpracticum.ru', '45.86.181.122']


# CORS_ALLOWED_ORIGINS = [
#     'http://localhost',
# ]
# CORS_ORIGIN_WHITELIST = ('http://localhost',)
CORS_ALLOW_ALL_ORIGINS = DEBUG

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    "corsheaders",
    'user.apps.UserConfig',
    'education',
    'kinder_guide',
    'comments',
    'about_us',
    'news',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.common.CommonMiddleware',

]

ROOT_URLCONF = 'kinder_guide.urls'

TEMPLATES_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'kinder_guide.wsgi.application'


if LOCAL_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    print('Sqlite3 database configured')

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'kinder_guide'),
            'USER': os.getenv('POSTGRES_USER', 'kinder_guide_user'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
            'HOST': os.getenv('DB_HOST', ''),
            'PORT': os.getenv('DB_PORT', 5432)
        }
    }
    print('PostgreSQL database configured')


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'collected_static'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.MyUser'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.IsAuthenticated'
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,
}

SIMPLE_JWT = {
    # 'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USERS': False,
    "USER_CREATE_PASSWORD_RETYPE": False,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    'PASSWORD_RESET_CONFIRM_URL': 'api/auth/reset/confirm//{uid}/{token}',
    'SEND_CONFIRMATION_EMAIL': True,
    'SERIALIZERS': {
        'current_user': 'user.serializers.CustomUserSerializer',
        'user_create': 'djoser.serializers.UserCreateSerializer',
        'user_delete': 'user.serializers.CusstomUserDeleteSerializer'
    },
    'PERMISSIONS': {
        'user_create': ['rest_framework.permissions.AllowAny'],
        'user': ['djoser.permissions.CurrentUserOrAdminOrReadOnly'],
        'password_reset': ['rest_framework.permissions.AllowAny'],
        'password_reset_confirm': ['rest_framework.permissions.AllowAny'],
        'user_delete': ['rest_framework.permissions.CurrentUserOrAdmin'],
        'token_create': ['rest_framework.permissions.AllowAny'],
    }
}

# Email settings

EMAIL_BACKEND_NAME = "KinderGuide@yandex.ru"
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


if LOCAL_EMAIL:

    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True

    EMAIL_HOST_USER = "KinderGuide@yandex.ru"
    EMAIL_HOST_PASSWORD = 'lirxjjyrfsotscvl'

    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
    SERVER_EMAIL = EMAIL_HOST_USER
else:
    EMAIL_HOST = 'skvmrelay.netangels.ru'
    EMAIL_PORT = 25

EMAIL_ADMIN = EMAIL_BACKEND_NAME
DEFAULT_FROM_EMAIL = EMAIL_BACKEND_NAME

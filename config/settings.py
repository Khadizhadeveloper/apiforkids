from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-gwe5@swe#2l6n)^e-n8)cwrp6jox6&v@_g@i6#05b#gp-hpz#9'

DEBUG = True

ALLOWED_HOSTS = ['*']  # ✅ Разрешаем запросы отовсюду (для тестов)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ Django Rest Framework
    'rest_framework',

    # ✅ Swagger (drf-spectacular)
    'drf_spectacular',
    'drf_spectacular_sidecar',

    # ✅ Наше приложение
    'users',
]

# ✅ Исправленный DRF (Swagger + JSON Renderer)
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # ✅ Была ошибка в названии
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',  # JSON API (по умолчанию)
        'rest_framework.renderers.BrowsableAPIRenderer',  # Интерфейс API
    ],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # ✅ Шаблоны будут искаться в templates/
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

WSGI_APPLICATION = 'config.wsgi.application'

# ✅ Подключение базы данных (по умолчанию SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ✅ Настройки статических файлов
STATIC_URL = 'static/'

# ✅ Swagger: Генерация OpenAPI схемы
SPECTACULAR_SETTINGS = {
    'TITLE': 'My API',
    'DESCRIPTION': 'Документация API',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

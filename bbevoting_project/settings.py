import os, math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '9%k^*0(qi*oktfa+#a3pp9g3eo-9vd(kws8+$t#lf2u&b#+u-*'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'ballot',
    'simulation',
    'welcome',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bbevoting_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', ],
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

WSGI_APPLICATION = 'bbevoting_project.wsgi.application'

# AUTH_USER_MODEL = "simulation.User"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'voting_db',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# PUZZLE
PUZZLE = '0000'  # or more zeros
PLENGTH = len(PUZZLE)

# BATCH SIMULATION
N_TRANSACTIONS = 100
N_TX_PER_BLOCK = 20
N_BLOCKS = math.ceil(N_TRANSACTIONS / N_TX_PER_BLOCK)  # Number of required blocks as int

# FOR DEMO PURPOSE
# IMPORTANT: Re-run the simulation after modifying these values.
# Public key
# PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
# MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEJ5r+Cab+pDjJm1INuWDJFfTPcvqJ
# lIEPNL/gFRyz9sl55N8jENmCslOSpNCkJUEb879x+0Jx0pg9POeOAT7Xrw==
# -----END PUBLIC KEY-----"""

PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE84ZZpVnAIumlPdn57BslwBSbz4Dx
uGzb52JQTVRdSLafA2nZ4tsjVxA6atcjofW0MSthNvPfi4oxbDjY82YzmQ==
-----END PUBLIC KEY-----"""

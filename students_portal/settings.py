"""
Django settings for students_portal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'a7ipc^72h1-wu78sn5@@tk+ea49iwn9atar!0*b3)2%%17(tge'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['students-portal.net', 'www.students-portal.net', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'forum',
    'hallway',
    'films',
    'library',
    'mixins',
    'ckeditor',
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

ROOT_URLCONF = 'students_portal.urls'

WSGI_APPLICATION = 'students_portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database/mainDataBase.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = 'pillow'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)

LOGIN_URL = '/account/login/'

CKEDITOR_JQUERY_URL = '/static/scripts/jquery.min.js'

CKEDITOR_CONFIGS = {
    "default": {
        'toolbar': [
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-',
             'TextColor', 'BGColor', '-',
             'NumberedList', 'BulletedList', '-',
             'Smiley', 'SpecialChar', '-',
             'Undo', 'Redo', '-',
             'Maximize']
        ],
        'forcePasteAsPlainText': True,
        'allowedContent': True,
        'height': 150,
        'width': 500,
        'undoStackSize': 50,
        'toolbarLocation': 'top',
        'tabSpaces': 4,
        'smiley_columns': 7,
        'enterMode': 2,  # br
        'shiftEnterMode': 1,  # p
        'autoParagraph': False,


        # 'toolbar_Full': [
        #   ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat' ],
        #   ['Image', 'Flash', 'Table', 'HorizontalRule'],
        #   ['TextColor', 'BGColor'],
        #   ['Smiley','sourcearea', 'SpecialChar'],
        #   [ 'Link', 'Unlink', 'Anchor' ],
        #   [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ],
        #   [ 'Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates' ],
        #   [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ],
        #   [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ],
        #   [ 'Maximize', 'ShowBlocks' ]
        #],
    }
}
from .common import *

DEBUG = False

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIr, 'media')

DATABASES = {
    'default' :{
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'gaeunyang.mysql.pythonanywhere-services.com',
        'NAME': 'gaeunhang$default',
        'USER': 'gaeunyang',
        'PASSWORD': 'yang1997',
        'OPTION' :
    }
}
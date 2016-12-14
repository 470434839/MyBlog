from .base import *

DEBUG = False

# INSTALLED_APPS += ["debug_toolbar", ]

ALLOWED_HOSTS = ['localhost', ]

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)

PAGE_SIZE = 2

SECRET_KEY = "you secret key"

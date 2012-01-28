from settings import *

DEBUG = False

CACHES = { 
    'default': { 
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache', 
        'LOCATION': '{host}:11211'.format(host=os.environ.get('MEMCACHE_SERVERS')), 
        'username': os.environ.get('MEMCACHE_USERNAME'), 
        'password': os.environ.get('MEMCACHE_PASSWORD') 
    } 
} 


STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAI3FAOQGNLNXPLP4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'chrisamywedding'

STATIC_URL = 'http://chrisamywedding.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = 'http://chrisamywedding.s3.amazonaws.com/admin/'
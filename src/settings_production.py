from settings import *
from S3 import CallingFormat

DEBUG = True

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAI3FAOQGNLNXPLP4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'chrisamywedding'

STATIC_URL = 'http://cdn.chrisamywedding.ca/'
ADMIN_MEDIA_PREFIX = 'http://cdn.chrisamywedding.ca/admin/'
MEDIA_URL = "http://cdn.chrisamywedding.ca/media/"
CMS_MEDIA_URL = "/cms/"
CMS_MEDIA_ROOT = "/"

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}

AWS_CALLING_FORMAT = CallingFormat.VANITY
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = 'cdn.chrisamywedding.ca'
AWS_S3_SECURE_URLS = False
from settings import *
from S3 import CallingFormat

DEBUG = False

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAI3FAOQGNLNXPLP4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'chrisamywedding'

STATIC_URL = 'http://chrisamywedding.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = 'http://chrisamywedding.s3.amazonaws.com/admin/'
MEDIA_URL = "http://chrisamywedding.s3.amazonaws.com/media/"
CMS_MEDIA_URL = "http://chrisamywedding.s3.amazonaws.com/cms/"

#AWS_HEADERS = {
#    'Cache-Control': 'max-age=1',
#}

AWS_CALLING_FORMAT = CallingFormat.VANITY
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = 'chrisamywedding.s3.amazonaws.com'
AWS_S3_SECURE_URLS = False

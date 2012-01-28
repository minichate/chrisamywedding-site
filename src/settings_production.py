from settings import *

DEBUG = False

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAI3FAOQGNLNXPLP4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'chrisamywedding'

STATIC_URL = 'http://static.chrisamywedding.ca/'
ADMIN_MEDIA_PREFIX = 'http://static.chrisamywedding.ca/admin/'
MEDIA_URL = "http://static.chrisamywedding.ca/media/"
CMS_MEDIA_URL = "http://static.chrisamywedding.ca/cms/"

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
from settings import *

DEBUG = False

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = 'AKIAI3FAOQGNLNXPLP4A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'chrisamywedding'

STATIC_URL = 'https://chrisamywedding.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = 'https://chrisamywedding.s3.amazonaws.com/admin/'
MEDIA_URL = "https://chrisamywedding.s3.amazonaws.com/media/"

AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
}
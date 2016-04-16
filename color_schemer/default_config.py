import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'TESTSTS')

DB_NAME = os.environ.get('POSTGRES_DB', None)
DB_USER = os.environ.get('POSTGRES_USER', None)
DB_PASS = os.environ.get('POSTGRES_PASSWORD', None)
DB_SERVICE = os.environ.get('POSTGRES_SERVICE', None)
DB_PORT = os.environ.get('POSTGRES_PORT', None)

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', None)

GOOGLE_CONSUMER_KEY = os.environ.get('GOOGLE_CONSUMER_KEY', None)
GOOGLE_CONSUMER_SECRET = os.environ.get('GOOGLE_CONSUMER_SECRET', None)

SQLALCHEMY_TRACK_MODIFICATIONS = False
LOG_LEVEL = 'DEBUG'
DEBUG = True

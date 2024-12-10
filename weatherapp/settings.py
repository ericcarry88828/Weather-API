from os import environ
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = environ.get('SECRET_KEY')
API_KEY = environ.get('API_KEY')
API_URL = environ.get('API_URL')
GEO_URL = environ.get('GEO_URL')
FLASK_APP = environ.get('FLASK_APP')
FLASK_DEBUG = environ.get('FLASK_DEBUG')
REDIS_HOST = environ.get('REDIS_HOST')
REDIS_USERNAME = environ.get('REDIS_USERNAME')
REDIS_PASSWORD = environ.get('REDIS_PASSWORD')
REDIS_PORT = environ.get('REDIS_PORT')
DATA_EXPIRE = environ.get('DATA_EXPIRE')

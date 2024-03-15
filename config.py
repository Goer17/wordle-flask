DATABASE_HOSTNAME = 'db'
DATABASE_PORT     = 3306
DATABASE = 'wordle'
USERNAME = 'root'
PASSWORD = 'password'
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{DATABASE_HOSTNAME}:{DATABASE_PORT}/{DATABASE}'

SQLALCHEMY_TRACK_MODIFICATIONS = True

import os

SECRET_KEY = os.urandom(16)
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "postgresql://test@localhost/test" if 'DATABASE_URL' not in os.environ else os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
ERROR_404_HELP = False

AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

JWT_SECRET = os.environ['JWT_SECRET']
JWT_EXPIRATION_DAYS = int(os.environ['JWT_EXPIRATION_DAYS'])

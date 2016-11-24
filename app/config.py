import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "consist dance excellent general"

SQLALCHEMY_DATABASE_URI = "postgresql://test@localhost/test" if 'SQL_DATABASE_URI' not in os.environ else os.environ['SQL_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
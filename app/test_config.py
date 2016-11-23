import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "you-will-never-guess"

SQLALCHEMY_DATABASE_URI = "postgresql://test@localhost/test"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
TESTING = True
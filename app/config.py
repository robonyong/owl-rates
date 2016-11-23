import os
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET_KEY = "you-will-never-guess"

SQLALCHEMY_DATABASE_URI = "postgresql://test@localhost/test" if 'SQL_DATABASE_URI' not in os.environ else os.environ['SQL_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

AWS_BUCKET = 'owl-rates'
AWS_ACCESS_KEY_ID = 'AKIAJWNJVURCD5NG6GKQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_DOMAIN_NAME = 's3-website-us-west-1.amazonaws.com'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

def create_app(conf):
  app = Flask(__name__)
  app.config.from_pyfile(conf)

  # Dynamically bind SQLAlchemy to application
  db.init_app(app)
  app.app_context().push()
  db.create_all()

  from app.views import public_pages
  app.register_blueprint(public_pages)

  return app

# app = Flask(__name__)
# app.config.from_pyfile('config.py', silent=True)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# db.create_all()


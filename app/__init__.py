from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

def create_test_app():
  app = Flask(__name__)
  app.config.from_pyfile('test-config.py', silent=True)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # Dynamically bind SQLAlchemy to application
  db.init_app(app)
  app.app_context().push() # this does the binding

  from app.views import public_pages
  app.register_blueprint(public_pages)

  return app

# you can create another app context here, say for production
def create_production_app():
  app = Flask(__name__)
  app.config.from_pyfile('config.py', silent=True)
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  # Dynamically bind SQLAlchemy to application
  db.init_app(app)
  app.app_context().push()

  from app.views import public_pages
  app.register_blueprint(public_pages)

  return app

# app = Flask(__name__)
# app.config.from_pyfile('config.py', silent=True)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
# db.create_all()


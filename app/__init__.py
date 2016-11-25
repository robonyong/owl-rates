from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

def create_app(conf):
  global db
  global api
  app = Flask(__name__)
  app.config.from_pyfile(conf)

  # Dynamically bind SQLAlchemy to application
  db.init_app(app)
  app.app_context().push()
  db.create_all()

  from app.routes import main, api_bp
  app.register_blueprint(main)
  app.register_blueprint(api_bp)

  return app
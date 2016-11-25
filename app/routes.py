from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for, jsonify
from flask_restful import Resource, Api
from database.api_resources import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

main = Blueprint('main', __name__, template_folder='templates')
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
	return render_template('index.html')

api.add_resource(OwlsApi, '/api/owls.json')
api.add_resource(OwlApi, '/api/owls/<int:owl_id>.json')
api.add_resource(Api404, '/api/<path:path>')
from flask import Blueprint, request, abort, render_template, make_response, flash, g, jsonify
from flask_restful import Resource, Api
from database.api_resources import *
from database.auth import attempt_login, create_account, refresh_token

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

main = Blueprint('main', __name__, template_folder='templates')
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

@main.route('/register', methods=['POST'])
def register():
  params = request.get_json(force=True)
  resp = create_account(params)
  return resp

@main.route('/login', methods=['POST'])
def login():
  params = request.get_json(force=True)
  resp = attempt_login(params)
  return resp

@main.route('/refresh-token', methods=['GET'])
def refresh():
  token = request.headers.get('Authorization')
  resp = refresh_token(token)
  return resp

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
	return render_template('index.html')

api.add_resource(Owls_Api, '/api/owls.json')
api.add_resource(Owl_Api, '/api/owls/<int:owl_id>.json', '/api/owls/<string:owl_slug>.json')
api.add_resource(Reviewer_Account_Api, '/api/account.json')
api.add_resource(Reviewer_Api, '/api/reviewer/<int:reviewer_id>.json')
api.add_resource(Api_404, '/api/<path:path>')

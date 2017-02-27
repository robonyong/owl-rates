import jwt
import arrow
from flask import request, jsonify, make_response

from sqlalchemy.exc import IntegrityError

from app.config import JWT_SECRET, JWT_EXPIRATION_DAYS
from database import Reviewer
from database.utilities import to_dict
from app import db

def attempt_login(params):
  email = params.get('email')
  password = params.get('password')

  if not email or not password:
    err = jsonify({'message': 'Bad Request: email and password fields are required'})
    resp = make_response(err, 400)
    return resp

  reviewer = Reviewer.query.filter_by(email=email).first()
  if not reviewer or not reviewer.verify_password(password):
    err = jsonify({'message': 'Invalid email & password combination'})
    resp = make_response(err, 400)
    return resp

  reviewer_dict = to_dict(reviewer)
  resp = _prepare_token_response(reviewer_dict)

  return make_response(jsonify(resp))

def create_account(params):
  email = params.get('email')
  password = params.get('password')
  name = params.get('name')

  if not email or not password or not name:
    err = jsonify({'message': 'Email, password, and name are required.'})
    resp = make_response(err, 400)
    return resp

  try:
    new_reviewer = Reviewer(email=email, name=name)
    new_reviewer.hash_password(password)
    db.session.add(new_reviewer)
    db.session.commit()

    reviewer_dict = to_dict(new_reviewer)
    resp = _prepare_token_response(reviewer_dict)
  except IntegrityError as e:
    resp = make_response(jsonify({'message': 'An account with that email already exists. Try logging in instead.'}), 400)

  return resp

def _prepare_token_response(reviewer_data):
  reviewer_data.pop('password_hash', None)
  expires_at = arrow.utcnow().replace(days=+JWT_EXPIRATION_DAYS).timestamp
  payload = dict(reviewer_data, exp=expires_at)
  token = jwt.encode(payload, JWT_SECRET)
  return {'token': token.decode(), 'expires_at': expires_at}

def refresh_token(token):
  try:
    payload = jwt.decode(token, JWT_SECRET)
    reviewer = Reviewer.query.filter_by(id=payload['id']).first()
    reviewer_dict = to_dict(reviewer)
    resp = _prepare_token_response(reviewer_dict)
    return make_response(jsonify(resp))
  except Exception as e:
    return make_response(jsonify({}), 403)

def verify_token(token):
  try:
    payload = jwt.decode(token, JWT_SECRET)
    return True
  except Exception as e:
    return False

def login_required(fn):
  @wraps(fn)
  def decorated_function(*args, **kwargs):
    token = request.headers.get(token)
    if not verify_token(token):
      return make_response(jsonify({}), 403)
    return fn(*args, **kwargs)
  return decorated_function

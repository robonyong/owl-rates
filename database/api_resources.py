import decimal, datetime
from flask_restful import Resource
from flask import jsonify, make_response

from app import db
from database import *

def alchemyencoder(obj):
  """JSON encoder function for SQLAlchemy special classes."""
  if isinstance(obj, datetime.date):
      return obj.isoformat()
  elif isinstance(obj, decimal.Decimal):
      return float(obj)

def to_dict(obj):
  obj.__dict__.pop('_sa_instance_state', None)
  return obj.__dict__

class Owls_Api(Resource):
  def get(self):
    owl_list = list(Owl.query.all())
    owls = list(map(to_dict, owl_list))
    return jsonify(owls)

class Owl_Api(Resource):
  def get(self, owl_id=None, owl_slug=None):
    useSlug = owl_id is None and owl_slug is not None
    query = Owl.slug==owl_slug if useSlug else Owl.id==owl_id
    value = owl_slug if useSlug else owl_id
    key = 'slug' if useSlug else 'id'
    try:
      owl = Owl.query.filter(query).first()
      if owl is None:
        owl = {'error': 'No owl with {} {} found'.format(key, value)}
        status_code = 404
        return make_response(jsonify(owl), status_code)
      status_code = 200
      descriptions = list(map(to_dict, owl.descriptions))
      ratings = list(map(to_dict, owl.ratings))
      for rating in ratings:
        print(rating.reviewer)
      avg_rating = owl.avg_rating
      owl = to_dict(owl)
      owl['descriptions'] = descriptions
      owl['ratings'] = ratings
      owl['avg_rating'] = avg_rating
      return make_response(jsonify(owl), status_code)
    except:
      raise

class Api_404(Resource):
  def return_not_found_api(self, path):
    error = {
      'error': path + ' endpoint not found'
    }
    return make_response(jsonify(error), 404)
  def get(self, path):
    return self.return_not_found_api(path)
  def post(self, path):
    return self.return_not_found_api(path)
  def delete(self, path):
    return self.return_not_found_api(path)
  def put(self, path):
    return self.return_not_found_api(path)

import decimal, datetime
from database import *
from flask_restful import Resource
from flask import jsonify, make_response

def alchemyencoder(obj):
  """JSON encoder function for SQLAlchemy special classes."""
  if isinstance(obj, datetime.date):
      return obj.isoformat()
  elif isinstance(obj, decimal.Decimal):
      return float(obj)

def to_dict(obj):
	obj.__dict__.pop('_sa_instance_state', None)
	return obj.__dict__

class OwlsApi(Resource):
	def get(self):
		owl_list = list(Owl.query.all())
		owls = list(map(to_dict, owl_list))
		return jsonify(owls)

class OwlApi(Resource):
	def get(self, owl_id):
		try:
			owl = Owl.query.filter(Owl.id==owl_id).first()
			status_code = 200 if owl is not None else 404
			owl = to_dict(owl) if owl is not None else {'error': 'No owl with id {} found'.format(owl_id)}
			return make_response(jsonify(owl), status_code)
		except:
			raise

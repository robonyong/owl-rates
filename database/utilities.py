import decimal, datetime

def alchemyencoder(obj):
  """JSON encoder function for SQLAlchemy special classes."""
  if isinstance(obj, datetime.date):
    return obj.isoformat()
  elif isinstance(obj, decimal.Decimal):
    return float(obj)
  return obj

def to_dict(obj):
  obj.__dict__.pop('_sa_instance_state', None)
  obj_dict = {}
  for k, v in obj.__dict__.items():
    obj_dict[k] = alchemyencoder(v)

  return obj_dict

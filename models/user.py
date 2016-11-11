from mongoengine import *
import datetime

class User(Document):
	name = StringField(required=True)
	email = EmailField(required=True, unique=True)
	authId = StringField(unique=True)
	ratings = ListField(ReferenceField('Rating'), default=list)
	owls = ListField(ReferenceField('Owl'), default=list)
	created = DateTimeField(default=datetime.datetime.now)
	updated = DateTimeField(default=datetime.datetime.now)
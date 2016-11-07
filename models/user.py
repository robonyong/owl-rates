from mongoengine import *
import datetime

class User(Document):
	name = StringField(required=True)
	email = EmailField(required=True)
	authId = StringField()
	ratings = ListField(ReferenceField('Rating'))
	review_owls = ListField(ReferenceField('Owl'))
	created = DateTimeField(default=datetime.datetime.now)
	updated = DateTimeField(default=datetime.datetime.now)
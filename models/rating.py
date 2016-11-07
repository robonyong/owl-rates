from mongoengine import *
import datetime

class Rating(Document):
	rating = IntField(min_value=0, max_value=10, required=True)
	review = StringField()
	user = ReferenceField('User')
	owl = ReferenceField('Owl', required=True)
	created = DateTimeField(default=datetime.datetime.now)
	updated = DateTimeField(default=datetime.datetime.now)
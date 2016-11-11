from mongoengine import *
import datetime

class Owl(Document):
	# _id = ObjectIdField()
	name = StringField(required=True)
	description = ListField(StringField(), required=True)
	image = URLField(required=True)
	image_web = URLField()
	image_thumbnail = URLField()
	ratings = ListField(ReferenceField('Rating'), default=list)
	avg_rating = DecimalField(min_value=0, max_value=10,precision=1)
	created = DateTimeField(default=datetime.datetime.now)
	updated = DateTimeField(default=datetime.datetime.now)
from app import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.sql import *
from passlib.apps import custom_app_context as pwd_context

assigned_owls = db.Table('assigned_owls',
	db.Column('owl_id', db.Integer, db.ForeignKey('owl.id')),
	db.Column('reviewer_id', db.Integer, db.ForeignKey('reviewer.id'))
)

class Owl(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	slug = db.Column(db.String(24), unique=True)
	nas_link = db.Column(db.String(140), unique=True)
	descriptions = db.relationship('OwlDescription', backref='owl', lazy='dynamic', order_by='OwlDescription.idx')
	image = db.Column(db.String(100), nullable=False)
	image_web = db.Column(db.String(100))
	image_thumbnail = db.Column(db.String(100))
	ratings = db.relationship('Rating', backref='owl', lazy='dynamic', cascade='delete')
	created = db.Column(db.DateTime, default=datetime.now)
	updated = db.Column(db.DateTime, default=datetime.now)

	@hybrid_property
	def avg_rating(self):
		ratings = [rating.rating for rating in self.ratings]
		return float(sum(ratings)) / max(len(ratings), 1)
	@avg_rating.expression
	def avg_rating(cls):
		return (select([func.avg(Rating.rating)]).
			where(Rating.owl_id == cls.id).
			label('avg_rating')
		)

	def __repr__(self):
		return '<Owl #{} {}>'.format(self.id, self.name)

class OwlDescription(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	owl_id = db.Column(db.Integer, db.ForeignKey('owl.id'), nullable=False)
	idx = db.Column(db.Integer, nullable=False)
	created = db.Column(db.DateTime, default=datetime.now)
	updated = db.Column(db.DateTime, default=datetime.now)
	__table_args__ = (
		db.UniqueConstraint('owl_id', 'idx', name='_owl_idx_uc'),
		{})

class Reviewer(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	email = db.Column(db.String(100), unique=True, nullable=False)
	password_hash = db.Column(db.String(128))
	ratings = db.relationship('Rating', backref='reviewer', lazy='dynamic', cascade='delete')
	owls = db.relationship('Owl', secondary=assigned_owls)
	created = db.Column(db.DateTime, default=datetime.now)
	updated = db.Column(db.DateTime, default=datetime.now)
	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)
		
	def __repr__(self):
		return '<Reviewer #{} {}>'.format(self.id, self.name)

class Rating(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	rating = db.Column(db.Integer, nullable=False)
	review = db.Column(db.Text)
	owl_id = db.Column(db.Integer, db.ForeignKey('owl.id'), nullable=False)
	reviewer_id = db.Column(db.Integer, db.ForeignKey('reviewer.id'))
	created = db.Column(db.DateTime, default=datetime.now)
	updated = db.Column(db.DateTime, default=datetime.now)
	__table_args__ = (
		db.CheckConstraint('rating >= 0 and rating <= 10', name='check_rating_range'),
		db.UniqueConstraint('owl_id', 'reviewer_id', name='_owl_reviewer_uc'),
		{})
	def __repr__(self):
		return '<Rating for owl {} with rating {}>'.format(self.owl_id, self.rating)
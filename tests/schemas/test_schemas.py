import pytest
from mongoengine import errors
from bson import ObjectId
from models import *

@pytest.mark.usefixtures("db")

class TestInsert:
	def test_insert_rating(db):
		rating = Rating(owl="5820191b4b8b2ad697accb0a", user="582024474b8b2ad697accb0c", rating=10)
		rating.save()
		assert Rating.objects(owl="5820191b4b8b2ad697accb0a", rating=10).count() == 1
		assert Owl.objects(id="5820191b4b8b2ad697accb0a", ratings__size=3).count() == 1
		assert User.objects(id="582024474b8b2ad697accb0c", ratings__size=4).count() == 1

	def test_insert_invalid_rating(db):
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			rating = Rating(owl="5820191b4b8b2ad697accb0a")
			rating.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			rating = Rating(owl="5820191b4b8b2ad697accb0a", rating=11)
			rating.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			rating = Rating(rating=5)
			rating.save()

	def test_insert_owl(db):
		owl = Owl(name="Snowy Owl", description=["A","Single","Snowy Owl"], image="http://placeowl.com/400/500")
		owl.save()
		assert Owl.objects(name="Snowy Owl").count() == 1

	def test_insert_invalid_owl(db):
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			owl = Owl()
			owl.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			owl = Owl(name="Brown Owl")
			owl.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			owl = Owl(name="Brown Owl", description=[])
			owl.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			owl = Owl(name="Brown Owl", description=[""], image="owl_image")
			owl.save()

	def test_insert_user(db):
		user = User(name="Test", email="email@example.com", authId="3")
		user.save()
		assert User.objects(name="Test").count() == 1

	def test_insert_invalid_user(db):
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			user = User()
			user.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			user = User(name="Test")
			user.save()
		with pytest.raises(errors.ValidationError, message="Expecting ValidationError"):
			user = User(name="Test", email="email")
			user.save()
		with pytest.raises(errors.NotUniqueError, message="NotUniqueError"):
			user = User(name="Test", email="email@example.com")
			user.save()
		with pytest.raises(errors.NotUniqueError, message="NotUniqueError"):
			user = User(name="Test", email="email+1@example.com", authId="3")
			user.save()
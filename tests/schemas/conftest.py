import pytest
import json
from mongoengine import connect
from models import *

def load_data_from_json(json_path):
	with open(json_path) as f:
		return json.load(f)

@pytest.fixture(scope="module")
def db(request):
	connection = connect('test')
	test_owls = load_data_from_json('tests/fixtures/owl.json')
	test_ratings = load_data_from_json('tests/fixtures/rating.json')
	test_users = load_data_from_json('tests/fixtures/user.json')
	for test_owl in test_owls:
		owl = Owl(**test_owl)
		owl.save()
	for test_user in test_users:
		user = User(**test_user)
		user.save()
	for test_rating in test_ratings:
		rating = Rating(**test_rating)
		rating.save()
	yield connection
	connection.drop_database('test')
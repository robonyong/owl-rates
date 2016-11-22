from flask_testing import TestCase
from sqlalchemy.exc import *
from app import create_test_app, db
from database.schemas import *
import json
import logging

def load_data_from_json(json_path):
  with open(json_path) as f:
    return json.load(f)

class DBTest(TestCase):
  def create_app(self):
    # pass in test configuration
    return create_test_app()

  def setUp(self):
    db.create_all()
    test_owls = load_data_from_json('tests/fixtures/owl.json')
    test_descs = load_data_from_json('tests/fixtures/description.json')
    test_ratings = load_data_from_json('tests/fixtures/rating.json')
    test_reviewers = load_data_from_json('tests/fixtures/reviewer.json')
    test_assigned_owls = load_data_from_json('tests/fixtures/assigned_owls.json')
    for test_owl in test_owls:
      owl = Owl(**test_owl)
      db.session.add(owl)

    for test_desc in test_descs:
      desc = OwlDescription(**test_desc)
      db.session.add(desc)

    for test_reviewer in test_reviewers:
      reviewer = Reviewer(**test_reviewer)
      db.session.add(reviewer)

    for test_rating in test_ratings:
      rating = Rating(**test_rating)
      db.session.add(rating)

    for assignment in test_assigned_owls:
      assigned_owls.insert().values(assignment)

    db.session.commit()

  def tearDown(self):

    db.session.remove()
    db.drop_all()

class TestInsert(DBTest):
  
  def test_insert_owl(self):
    owl = Owl(name="New Owl", image="http://placeowl.com/300/400")
    db.session.add(owl)
    db.session.commit()
    assert Owl.query.count() == 4

  def test_insert_invalid_owl(self):
    owl = Owl(name="Another Owl")
    db.session.add(owl)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

    owl = Owl()
    db.session.add(owl)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

  def test_insert_description(self):
    description = OwlDescription(description="A new description", owl_id=1, idx=1)
    db.session.add(description)
    db.session.commit()
    owl = Owl.query.filter_by(id=1).first()
    assert OwlDescription.query.count() == 5
    assert len(list(owl.descriptions)) == 2
    assert owl.descriptions[1] == description

  def test_insert_invalid_desription(self):
    description = OwlDescription(description="A new new description", owl_id=2, idx=1)
    db.session.add(description)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

    description = OwlDescription(description="A new new description", idx=1)
    db.session.add(description)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

    description = OwlDescription()
    db.session.add(description)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

  def test_insert_rating(self):
    rating = Rating(rating=9, owl_id=3)
    db.session.add(rating)
    db.session.commit()
    owl = Owl.query.filter(Owl.id==3).first()
    assert Rating.query.count() == 7
    assert len(list(owl.ratings)) == 3
    assert owl.avg_rating == 7.0

  def test_insert_invalid_rating(self):
    rating = Rating(rating=11, owl_id=3)
    db.session.add(rating)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

    rating = Rating(rating=9, owl_id=3, reviewer_id=2)
    db.session.add(rating)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()
    
    rating = Rating()
    db.session.add(rating)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

  def test_insert_reviewer(self):
    reviewer = Reviewer(name="Test", email="example@example.com")
    db.session.add(reviewer)
    db.session.commit()
    assert Reviewer.query.count() == 3
    assert Reviewer.query.order_by(Reviewer.id.desc()).first() == reviewer

  def test_insert_invalid_reviewer(self):
    reviewer = Reviewer(name="Another Test")
    db.session.add(reviewer)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

    reviewer = Reviewer()
    db.session.add(reviewer)
    self.assertRaises(IntegrityError, db.session.commit)
    db.session.rollback()

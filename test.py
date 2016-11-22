import unittest
import flask_testing

if __name__ == '__main__':
	suite = unittest.TestLoader().discover('./tests', pattern='test_*.py')
	unittest.TextTestRunner(verbosity=2).run(suite)
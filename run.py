from app import create_app, db
from database.schemas import *

if __name__ == '__main__':
	app = create_app('config.py')
	app.run(debug=True)
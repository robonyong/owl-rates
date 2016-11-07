from flask import Flask
import config
from mongoengine import connect
from bson.objectid import ObjectId
from models import *

app = Flask(__name__)
app.config.from_object('config')

connect("test")

@app.route('/')
def hello_world():
	return 'Hello world'

if __name__ == '__main__':
    app.run()
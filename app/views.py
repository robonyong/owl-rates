from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from database import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

public_pages = Blueprint('public_pages', __name__, template_folder='templates')

@public_pages.route('/')
@public_pages.route('/index')
def hello_world():
	return 'Hello world'

@public_pages.route('/owls')
def show_owls():
	return render_template("owls/all.html", owls=Owl.query.filter())
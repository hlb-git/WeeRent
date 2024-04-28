#!/usr/bin/python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from weerent.models import User, Accomodation, Image


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:weerentflask200@localhost/weerent'
db = SQLAlchemy(app)


with app.app_context():
    db.create_all()

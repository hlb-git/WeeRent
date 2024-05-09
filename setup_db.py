#!/usr/bin/python3
"""
This script
initializes the database
and creates the needed tables
"""
from flask_sqlalchemy import SQLAlchemy
from weerent.models import User, Accomodation, Image
from weerent import db, app



with app.app_context():
    db.create_all()

"""
In addition to the above script, please run the commands below in your
mysql server to create a user for sqlalchemy

Commands:

CREATE DATABASE weerent;
CREATE USER 'test'@'localhost' IDENTIFIED BY 'weerentflask200';
GRANT ALL PRIVILEGES ON weerent.* TO 'test'@'localhost';


"""

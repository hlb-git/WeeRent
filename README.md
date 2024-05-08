# WeeRent
Collaborative Portfolio Project That Aims to Solve Accommodation Problems for Corps Members

Getting Started
run ./dependencies.sh // for linux users
run ./mac_dep.sh // for mac users

"""
In addition to the above dependencies script, please run the commands below in your
mysql server to create a user for sqlalchemy
"""
Commands

CREATE DATABASE weerent;
CREATE USER 'test'@'localhost' IDENTIFIED BY 'weerentflask200';
GRANT ALL PRIVILEGES ON weerent.* TO 'test'@'localhost';

python3 setub_db.py

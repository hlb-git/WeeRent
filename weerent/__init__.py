from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'fc8f3aa817427b9a83648d17332fab8484fc1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from weerent import routes

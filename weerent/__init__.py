from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from weerent.states_and_towns import states_and_towns



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'fc8f3aa817427b9a83648d17332fab8484fc1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:weerentflask200@localhost/weerent'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


state_dropdown = [(state, state) for state in states_and_towns.keys()]
state_dropdown = [('', '(Select State)')] + state_dropdown


from weerent import routes
from weerent import errors

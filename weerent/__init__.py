from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import requests



app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SECRET_KEY'] = 'fc8f3aa817427b9a83648d17332fab8484fc1f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test:weerentflask200@localhost/weerent'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


state_url = "https://nigeria-states-towns-lga.onrender.com/api/states"
all_url = "https://nigeria-states-towns-lga.onrender.com/api/all"

all_data = requests.get(all_url).json()
states_data = requests.get(state_url).json()

states_and_towns = {}


for state in states_data:
    current_state = state.get('name')
    towns = []
    for state_name in all_data:
        for town in state_name.get('towns'):
            if state_name.get('name') == current_state:
                towns.append(town.get('name'))
    states_and_towns[current_state] = towns

state_dropdown = [(state, state) for state in states_and_towns.keys()]
state_dropdown = [('(Select State)', '(Select State)')] + state_dropdown


from weerent import routes
from weerent import errors

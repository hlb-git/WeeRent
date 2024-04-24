from flask import render_template, url_for
from weerent import app
from weerent.forms import Register, Login

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About Us')

@app.route('/register')
def register():
    form = Register()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', title='Login', form=form)


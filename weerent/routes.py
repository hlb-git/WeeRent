from flask import render_template, url_for, flash, redirect
from weerent import app, db, bcrypt
from weerent.forms import Register, Login
from weerent.models import User, Accomodation, Image

@app.route('/')
@app.route('/home')
def home():
    """Home page route."""
    return render_template('home.html')

@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html', title='About Us')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register page route."""
    form = Register()
    if form.validate_on_submit():
        db.create_all()
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created successfully! Please log in.", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page route."""
    form = Login()
    return render_template('login.html', title='Login', form=form)

@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html', title='Contact Us')


from flask import render_template, url_for, flash, redirect
from weerent import app
from weerent.forms import Register, Login

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
        print('here')
        flash(f"Account created for {form.username.data} successfully!", 'success')
        return redirect(url_for('home'))
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


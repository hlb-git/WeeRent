from flask import render_template, url_for, flash, redirect, request
from weerent import app, db, bcrypt
from weerent.forms import Register, Login, New
from weerent.models import User, Accomodation, Image
from flask_login import login_user, logout_user, current_user, login_required


@app.route('/')
@app.route('/home')
def home():
    """Home page route."""
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register page route."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Register()
    if form.validate_on_submit():
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Login()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user and bcrypt.check_password_hash(existing_user.password,
                                                        form.password.data):
            login_user(existing_user, form.remember.data)
            next_page = request.args.get('next')
            flash(f"Log in successful!", 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f"Log in failed! Please recheck email and password.", 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/new', methods=['GET', 'POST'])
def new():
    """About page route."""
    form = New()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            accomodation = Accomodation(state=form.state.data,
                                        LGA=form.lga.data,
                                        city=form.city.data,
                                        address=form.city.data,
                                        house_type=form.type.data,
                                        details=form.details.data,
                                        landlord_id=current_user.id)
            db.session.add(accomodation)
            db.session.commit()
            for image in form.image.data:
                img = Image(data=image.filename, accomodation_id=accomodation.id)
                db.session.add(img)
                db.session.commit()
            flash(f"Rent added successfully!", 'success')
            return redirect(url_for('home'))
    else:
        flash(f"Please log in to add a new rent.", 'danger')
        return redirect(url_for('login'))
    return render_template('new.html', title='New Rent', form=form)

@app.route('/contact')
def contact():
    """Contact page route."""
    return render_template('contact.html', title='Contact Us')

@app.route('/logout')
def logout():
    """Logout route."""
    logout_user()
    return redirect(url_for('home'))

@app.route('/dashboard')
@login_required
def dashboard():
    """dashboard page route."""
    return render_template('dashboard.html', title='Dashboard')

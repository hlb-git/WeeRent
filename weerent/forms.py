from flask_wtf import FlaskForm
from weerent import state_dropdown
from weerent.models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from flask_wtf.file import MultipleFileField, FileAllowed
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


class Register(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        existingEmail = User.query.filter_by(email=email.data).first()
        if existingEmail:
            raise ValidationError('Email already exists!')


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class New(FlaskForm):
    state = SelectField('State', choices=state_dropdown,
                        validators=[DataRequired()])
    lga = StringField('Local Government Area', validators=[DataRequired()])
    city = StringField('City/ Town', validators=[DataRequired()])
    type = SelectField('Rent Type', choices=[('(Select Rent Type)', '(Select Rent Type)'),
                                              ('Single Room', 'Single Room'),
                                              ('Self Contain', 'Self Contain'),
                                              ('Flat', 'Flat'),
                                              ('Duplex', 'Duplex')],
                                              validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    details = TextAreaField('Rent Details (e.g Facilities)', validators=[DataRequired()])
    image = MultipleFileField('Upload Images', validators=[FileAllowed(['jpg', 'png', 'jpeg', 'gif'])])

    submit = SubmitField('Add Rent')

class Filter(FlaskForm):
    state = SelectField('State', choices=state_dropdown)
    city = StringField('City/ Town', render_kw={"placeholder": "Enter City"})
    type = SelectField('Rent Type', choices=[('', '(Select Rent Type)'),
                                              ('Single Room', 'Single Room'),
                                              ('Self Contain', 'Self Contain'),
                                              ('Flat', 'Flat'),
                                              ('Duplex', 'Duplex')])
    submit = SubmitField('Filter')


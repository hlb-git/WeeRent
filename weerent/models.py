"""User model module."""
from weerent import db, app
from weerent.superclass import Superclass


class User(Superclass, db.Model):
    """The User class."""
    __tablename__ = 'users'
    firstname = db.Column(db.String(60), nullable=False)
    lastname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    accomodations = db.relationship('Accomodation', backref='landlord', lazy=True)
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"""
    Class: {self.__class__.__name__}
    Id: {self.id}
    Full Name: {self.firstname} {self.lastname}
    Email: {self.email}
    Date Registered: {self.createdAt}
    """


class Accomodation(Superclass, db.Model):
    """The Accomodation class."""
    __tablename__ = 'accomodations'
    state = db.Column(db.String(60), nullable=False)
    LGA = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    house_type = db.Column(db.String(60), nullable=False)
    details = db.Column(db.Text, nullable=False)
    landlord_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    images = db.relationship('Image', backref='accomodation',
                             lazy=True, cascade='all, delete, delete-orphan')

    def __repr__(self):
        return f"""
    Class: {self.__class__.__name__}
    Id: {self.id}
    Full Address: {self.address}, {self.LGA}, {self.state}.
    Type: {self.house_type}
    Landlor Id: {self.landlord_id}
    """

class Image(Superclass, db.Model):
    """The Images class."""
    __tablename__ = 'images'
    data = db.Column(db.String(60))
    accomodation_id = db.Column(db.String(60), db.ForeignKey('accomodations.id'), nullable=False)


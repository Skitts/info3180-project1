from . import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    biography= db.Column(db.String(80))
    gender = db.Column(db.String(80))
    image = db.Column(db.LargeBinary)
    datejoined = db.Column(db.DateTime)
    
    
    def __init__(self, id, firstname, lastname, username,age,biography,gender,image,datejoined):
        self.id
        self.firstname
        self.lastname
        self.username
        self.age
        self.biography
        self.gender
        self.image
        self.datejoined
        
        
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)

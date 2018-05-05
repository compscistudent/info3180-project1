from . import db
from werkzeug.security import generate_password_hash


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    #__tablename__ = 'user_profiles'

    userid = db.Column(db.Integer, unique=True, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(6))
    bio = db.Column(db.String(255))
    image = db.Column(db.String(255))
    created_on = db.Column(db.DateTime())
    

    def __init__(self, first_name, last_name, username, userid, age, gender, bio, image, created_on):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.userid=userid
        self.age = age
        self.gender = gender
        self.bio = bio
        self.image = image
        self.created_on= created_on        

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
        return '<User %r>' %  self.username

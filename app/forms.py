from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField, HiddenField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed

class ProfileForm(FlaskForm):
    firstname = StringField('Firstname: ', validators=[DataRequired()])
    lastname = StringField('Lastname: ', validators=[DataRequired()])
    username = StringField('Username: ', validators=[DataRequired()])
    age = IntegerField('Age: ', validators=[DataRequired()])
    gender = SelectField('Gender: ', choices=[('', ''), ('Female', 'Female'),('Male', 'Male')])
    bio = StringField('Biography: ', validators=[DataRequired()])
    image = FileField('Profile Picture: ', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images Only')])
    

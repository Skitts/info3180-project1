from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, FileField,SelectField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class InfoForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    age = IntegerField('age', validators=[InputRequired()])
    biography = StringField('biography', validators=[InputRequired()])
    image = FileField('image', validators=[InputRequired()])
    gender = SelectField('gender', choices= [('Male', 'Male'),('Female','Female')], validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    
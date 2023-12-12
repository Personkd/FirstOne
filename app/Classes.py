from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,IntegerField,BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

class Register(FlaskForm):
    password = IntegerField("Password", validators=[DataRequired()])
    name = StringField("Name",  validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])

class Gameadd(FlaskForm):
    posttext = StringField('Write your post here', validators=[DataRequired()])
    button = SubmitField('Додати')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password =  StringField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    button = SubmitField('Enter')

class Login(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
    button = SubmitField('Enter')

class adminLogincheck(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password =  StringField('Password', validators=[DataRequired()])
    button = SubmitField('Enter')

class addgame(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    description =  StringField('Password', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    image =  StringField('Password', validators=[DataRequired()])
    button = SubmitField('Enter')
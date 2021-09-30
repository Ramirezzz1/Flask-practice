#imports that i'll need to work with wtforms: generic from template. 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DecimalField, PasswordField, BooleanField
from wtforms.validators import DataRequired #Length, EqualTo 

#create new form
class newActorForm(FlaskForm):
    #what we put inside this clas is whater data fields we intend our form to have
    name = StringField('Name', validators=[DataRequired()])
    hiringprice = StringField('Hiring Price')
    age = IntegerField('Age', validators=[DataRequired()])
    nationality = StringField('Nationality')
    best_film = StringField('Best Performance', validators=[DataRequired()])
    submit_button = SubmitField()

# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired(),Length(min=2, max=20)])
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
#     submit = SubmitField('Sign Up')

#     class LoginForm(FlaskForm):
#     email = StringField('Email', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember = BooleanField('Remember Me')
#     submit = SubmitField('Login')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired,length,Email,EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Please enter a valid email'),Email(message='please enter a valid email address')])
    password = PasswordField('Password', validators=[DataRequired(message='Please password')])
    submit = SubmitField('Login')

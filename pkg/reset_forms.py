from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField,EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo,Length, Regexp


class ResetForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(message='Please enter a valid email'),Email(message='please enter a valid email address')])
    new_password = PasswordField('New Password', validators=[DataRequired(),
    Length(min=8, message='Password must be at least 8 characters long'),Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', message='Password must include at least one lowercase letter, one uppercase letter, one number, and one special character')])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password', message='Password do not match')])
    submit = SubmitField('Reset Password')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, BooleanField, TextAreaField, DateField,SelectField, EmailField
from wtforms.validators import DataRequired, Email, URL, Length, EqualTo

from flask_wtf.file import MultipleFileField, FileAllowed, FileRequired
from pkg.models import State,Lga


class UploadImage(FlaskForm):
    pname = StringField('Property Name', validators=[DataRequired()])
    pdesc = TextAreaField('Property description', validators=[DataRequired()])
    amt = StringField('Amount', validators=[DataRequired()])
    paddress = TextAreaField('Property Address', validators=[DataRequired()])
    state = SelectField('State', coerce=int, validators=[DataRequired()])
    lga = SelectField('LGA', coerce=int, validators=[DataRequired()])
    type = SelectField('Property Type', coerce=int, validators=[DataRequired()])
    cat = SelectField('Category', coerce=int, validators=[DataRequired()])
    images = MultipleFileField('Choose Files', validators=[FileRequired('No file chosen!'),FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Submit')


    
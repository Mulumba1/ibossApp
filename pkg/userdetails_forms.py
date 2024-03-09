from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  TextAreaField, DateField,SelectField, EmailField
from wtforms.validators import DataRequired, Email



class UserdetailsForm(FlaskForm):
    email = EmailField('Email')
    ref = StringField('Ref No')
    submit = SubmitField('Submit')
   

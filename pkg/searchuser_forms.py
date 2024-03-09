from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class SearchuserForm(FlaskForm):
    email = StringField('User Email')
    ref = StringField('User Ref')
    submit = SubmitField('Search')

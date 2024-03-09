from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField


class ChangdpForm(FlaskForm):
    pics = FileField('Profile Image')
    submit = SubmitField('Upload Image')
    cancel = SubmitField('Cancel')
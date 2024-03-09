from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,  TextAreaField, DateField,SelectField, EmailField
from wtforms.validators import DataRequired, Email


class InitialCapitalStringField(StringField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0].strip().title()
        else:
            self.data = ''

class InitialCapitalTextAreaField(TextAreaField):
    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[0].strip().title()
        else:
            self.data = ''




class EditForm(FlaskForm):
    email = EmailField('Email', validators= [Email(message='Please enter a valid email address')])
    phone = StringField('Phone number')
    dob = DateField('Date of Birth')
    address = InitialCapitalTextAreaField('Residence Address',)
    state = SelectField('State', coerce=int)
    lga = SelectField('L G A', coerce=int)
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

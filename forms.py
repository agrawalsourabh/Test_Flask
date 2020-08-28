from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RegistrationForms(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email Address')
    submit = SubmitField()
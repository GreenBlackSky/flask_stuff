from flask_wtf import FlaskForm, RecaptchaField

from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message="Not a valid email."), DataRequired()])
    body = TextField('Message', [DataRequired(), Length(min=4, message="Message too short")])
    submit = SubmitField("Submit")


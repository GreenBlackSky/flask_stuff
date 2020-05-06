from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class AddItemForm(FlaskForm):
    key = StringField('Key', validators=[DataRequired()])
    value = StringField('Value', validators=[DataRequired()])
    submit = SubmitField('Add item')


class RemoveItemForm(FlaskForm):
    key = StringField('Key', validators=[DataRequired()])
    submit = SubmitField('Remove item')

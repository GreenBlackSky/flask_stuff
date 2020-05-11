from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired


class Add_Form(FlaskForm):
    num1 = IntegerField('num1', validators=[DataRequired()])
    num2 = IntegerField('num2', validators=[DataRequired()])
    submit = SubmitField('Register')

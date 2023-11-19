from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    age = IntegerField(label='Age', validators=[DataRequired()])
    submit_button = SubmitField(label='Submit')


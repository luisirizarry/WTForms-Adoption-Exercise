from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField, IntegerField, RadioField
from wtforms.validators import InputRequired, URL, NumberRange

class PetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('Cat', 'Cat'), ('Dog', 'Dog'),('Fish', 'Fish'),('Bird', 'Bird')], validators=[InputRequired()])
    photo_url = StringField("Photo URL", validators=[URL(message="Please enter a valid URL")])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30, message="Please enter a valid age between 0 and 30")])
    notes = StringField("Notes")
    available = BooleanField("Available")
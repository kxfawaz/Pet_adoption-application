from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Email , URL, Optional, Length, NumberRange


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name cannot be blank")])
    species = SelectField("Pet Species", choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')])
    photo_url = StringField("Photo Url", validators=[Optional(),URL()])
    age = FloatField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes",validators=[Optional(),Length(min=10)])
    
    
class EditPetForm(FlaskForm):
    photo_url = StringField("Photo Url", validators=[Optional(),URL()])
    notes = StringField("Notes",validators=[Optional(),Length(min=10)])
    available = BooleanField("Available?")

    
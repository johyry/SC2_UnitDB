from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators, IntegerField
from application.units.models import Unit
 

# Unitform

class UnitForm(FlaskForm):
    name = TextField("Unit name", [validators.Length(min=2)])
    supply = IntegerField("Supply", [validators.NumberRange(min=0, message='Input must be positive')])
    minerals = IntegerField("Minerals", [validators.NumberRange(min=0, message='Input must be positive')])
    gas = IntegerField("Gas", [validators.NumberRange(min=0, message='Input must be positive')])
    buildtime= IntegerField("Buildtime", [validators.NumberRange(min=0, message='Input must be positive')])

    class Meta:
        csrf = False


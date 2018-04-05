from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators

class UnitForm(FlaskForm):
    name = TextField("Unit name", [validators.Length(min=2)])
    supply = TextField("Supply", [validators.NumberRange(0, 10, message='Input must be positive')])
    minerals = TextField("Minerals", [validators.NumberRange(0, message='Input must be positive')])
    gas = TextField("Gas", [validators.NumberRange(0, message='Input must be positive')])
    buildtime= TextField("Buildtime", [validators.NumberRange(0, message='Input must be positive')])


#class EditUnitForm()
 
    class Meta:
        csrf = False

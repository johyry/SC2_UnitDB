from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators, IntegerField
from application.units.models import Unit
 

class BuildorderForm(FlaskForm):
    name = TextField("Buildorder name", [validators.Length(max=100, message="Input must be less than 100 characters")])
    description = StringField("Description", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    intro = StringField("Introduction", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    vod = StringField("VOD", [validators.Length(max=100, message='Input must be less than 100 characters')])
    details = StringField("Buildorder", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    analysis = StringField("Analysis", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])

    class Meta:
        csrf = False

class EditBuildorderForm(FlaskForm):
    name = TextField("Buildorder name", [validators.Length(min=2)])
    description = StringField("Description")
    intro = StringField("Introduction")
    vod = StringField("VOD", [validators.Length(max=100)])
    details = StringField("Buildorder")
    analysis = StringField("Analysis")
    
    class Meta:
        csrf = False
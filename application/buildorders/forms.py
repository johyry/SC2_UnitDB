from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators, IntegerField
from application.units.models import Unit
 

class BuildorderForm(FlaskForm):
    name = TextField("Buildorder name", [validators.Length(min=2)])
    description = StringField("Description")
    intro = StringField("Introduction")
    vod = StringField("VOD", [validators.Length(max=100)])
    details = StringField("Buildorder")
    analysis = StringField("Analysis")

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
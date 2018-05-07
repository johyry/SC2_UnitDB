from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators, IntegerField
from application.units.models import Unit
 


# New buildorder form

class BuildorderForm(FlaskForm):
    name = TextField("Buildorder name", [validators.Length(max=100, message="Input must be less than 100 characters")])

    buildtype = StringField("Build type", [validators.Length(max=30, message='Input must be less than 30 characters')])
    race = StringField("Race", [validators.Length(max=10, message='Input must be less than 10 characters')])

    description = StringField("Description", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    intro = StringField("Introduction", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    vod = StringField("VOD", [validators.Length(max=100, message='Input must be less than 100 characters')])
    details = StringField("Buildorder", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    analysis = StringField("Analysis", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])

    class Meta:
        csrf = False


# Edit buildorder form

class EditBuildorderForm(FlaskForm):
    name = TextField("Buildorder name", [validators.Length(max=100, message="Input must be less than 100 characters")])

    buildtype = StringField("Build type", [validators.Length(max=30, message='Input must be less than 30 characters')])
    race = StringField("Race", [validators.Length(max=10, message='Input must be less than 10 characters')])

    description = StringField("Description", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    intro = StringField("Introduction", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    vod = StringField("VOD", [validators.Length(max=100, message='Input must be less than 100 characters')])
    details = StringField("Buildorder", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    analysis = StringField("Analysis", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    
    class Meta:
        csrf = False
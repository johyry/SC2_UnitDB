from flask_wtf import FlaskForm
from wtforms import TextField, StringField, validators, IntegerField, TextAreaField
from application.units.models import Unit
 


# New buildorder form

class BuildorderForm(FlaskForm):
    name = TextAreaField("Buildorder name", [validators.Length(min=1, max=100, message="Input must be between 1 and 100 characters")])

    buildtype = TextAreaField("Build type", [validators.Length(max=30, message='Input must be less than 30 characters')])
    race = TextAreaField("Race", [validators.Length(max=10, message='Input must be less than 10 characters')])

    description = TextAreaField("Description", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    intro = TextAreaField("Introduction", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    vod = TextAreaField("VOD", [validators.Length(max=100, message='Input must be less than 100 characters')])
    details = TextAreaField("Buildorder", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])
    analysis = TextAreaField("Analysis", [validators.Length(max=10000, message='Input must be less than 10 000 characters')])

    class Meta:
        csrf = False



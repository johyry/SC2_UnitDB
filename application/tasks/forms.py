from flask_wtf import FlaskForm
from wtforms import TextField

class TaskForm(FlaskForm):
    name = TextField("Unit name")
    supply = TextField("Supply")
    minerals = TextField("Minerals")
    gas = TextField("Gas")
    buildtime= TextField("Buildtime")
 
    class Meta:
        csrf = False

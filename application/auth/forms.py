from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators 
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False


class CreateUserForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username", [
        validators.Regexp('\w+', message="Username must contain only letters numbers or underscore"),
        validators.Length(min=5, max=25, message="Username must be betwen 5 & 25 characters")

    ])
    password = PasswordField("Password",
        [
            validators.Length(min=2),
            validators.DataRequired(),
            validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeat password')

    class Meta:
        csrf = False
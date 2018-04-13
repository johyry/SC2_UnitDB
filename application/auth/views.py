from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import db
from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import CreateUserForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():

    logout_user()

    return redirect(url_for("index"))  


@app.route("/auth/createuser")
def auth_createuserform():

    return render_template("auth/createuserform.html", form = CreateUserForm())


@app.route("/auth/", methods=["POST"])
def auth_createuser():

    form = CreateUserForm(request.form)

    if not form.validate():
        return render_template("auth/createuserform.html", form = form)

    t = User(form.name.data, form.username.data, form.password.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("index"))





from application import app, db
from flask import render_template, request, redirect, url_for, abort
from application.buildorders.models import Buildorder
from application.buildorders.forms import BuildorderForm, EditBuildorderForm
from flask_login import login_required, current_user

@app.route("/buildorders", methods=["GET"])
def buildorders_index():
    return render_template("buildorders/list.html", buildorders = Buildorder.query.all())

@app.route("/buildorders/mybuildorders", methods=["GET"])
@login_required
def buildorders_myindex():
    
 
    return render_template("buildorders/list.html", buildorders = Buildorder.query.filter_by(account_id = current_user.id))

@app.route("/buildorders/new/")
@login_required
def buildorders_form():
    return render_template("buildorders/new.html", form = BuildorderForm())

@app.route("/buildorders/edit/<buildorder_id>/", methods=["GET", "POST"])
@login_required
def edit_buildorder(buildorder_id):

    if request.method == 'POST':
        

        buildorder = Buildorder.query.get(buildorder_id)
        
        form = EditBuildorderForm(request.form)

        if not form.validate():
            return render_template("buildorders/edit.html", form = form, buildorder = buildorder)

        buildorder.name = form.name.data
        buildorder.buildtype = form.buildtype.data
        buildorder.race = form.race.data
        buildorder.description = form.description.data
        buildorder.intro = form.intro.data
        buildorder.vod = form.vod.data
        buildorder.details = form.details.data
        buildorder.analysis = form.analysis.data


        

        db.session().commit()



        return redirect(url_for("buildorders_index"))

    buildorder = Buildorder.query.get(buildorder_id)
    form = EditBuildorderForm(request.form)
    

    if not buildorder:
        abort(403)
    
    form.name.data = buildorder.name
    form.buildtype.data = buildorder.buildtype
    form.race.data = buildorder.race
    form.description.data = buildorder.description
    form.intro.data = buildorder.intro
    form.vod.data = buildorder.vod
    form.details.data = buildorder.details
    form.analysis.data = buildorder.analysis


    
  
    return render_template("buildorders/edit.html", form = form, buildorder = buildorder)

@app.route("/buildorders/delete/<buildorder_id>/", methods=["GET"])
@login_required
def delete_buildorder(buildorder_id):

    buildorder = Buildorder.query.get(buildorder_id)
    db.session.delete(buildorder)
    db.session().commit()


    return redirect(url_for("buildorders_index"))

@app.route("/buildorders/", methods=["POST"])
@login_required
def buildorder_create():
    form = BuildorderForm(request.form)
    
    if not form.validate():
        return render_template("buildorders/new.html", form = form)

    buildorder = Buildorder(form.name.data)
    buildorder.buildtype = form.buildtype.data
    buildorder.race = form.race.data
    buildorder.description = form.description.data
    buildorder.intro = form.intro.data
    buildorder.vod = form.vod.data
    buildorder.details = form.details.data
    buildorder.analysis = form.analysis.data
    buildorder.account_id = current_user.id

    

    db.session().add(buildorder)
    db.session().commit()
  
    return redirect(url_for("buildorders_index"))

@app.route("/buildorders/<buildorder_id>", methods=["GET"])
@login_required
def single_buildorder(buildorder_id):

    buildorder = Buildorder.query.get(buildorder_id)

    form = BuildorderForm(request.form)
    
    if not buildorder:
        abort(403)
    
    form.name.data = buildorder.name
    form.buildtype.data = buildorder.buildtype
    form.race.data = buildorder.race
    form.description.data = buildorder.description
    form.intro.data = buildorder.intro
    form.vod.data = buildorder.vod
    form.details.data = buildorder.details
    form.analysis.data = buildorder.analysis


    return render_template("buildorders/buildorder.html", form = form, buildorder = buildorder)

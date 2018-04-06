from application import app, db
from flask import render_template, request, redirect, url_for
from application.units.models import Unit
from application.units.forms import UnitForm, EditUnitForm
from flask_login import login_required, current_user


@app.route("/units", methods=["GET"])
def units_index():
    return render_template("units/list.html", units = Unit.query.all())

@app.route("/units/new/")
@login_required
def units_form():
    return render_template("units/new.html", form = UnitForm())

@app.route("/units/edit/<unit_id>/", methods=["POST", "GET"])
@login_required
def edit_unit(unit_id):

    unit = Unit.query.get(unit_id)
    form = EditUnitForm(unit)
    if request.method == 'POST':
        form.populate_obj(unit)
        unit.save
        redirect('edit_profile')
  
    return render_template("units/edit.html", form = form)

@app.route("/units/edit", methods=["POST"])
@login_required
def units_edit():



    return redirect(url_for("units_index"))

@app.route("/units/", methods=["POST"])
@login_required
def unit_create():
    form = UnitForm(request.form)
    
    if not form.validate():
        return render_template("units/new.html", form = form)

    t = Unit(form.name.data)
    t.supply = form.supply.data
    t.minerals = form.minerals.data
    t.gas = form.gas.data
    t.buildtime = form.buildtime.data

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("units_index"))

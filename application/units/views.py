from application import app, db
from flask import render_template, request, redirect, url_for, abort
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

@app.route("/units/edit/<unit_id>/", methods=["GET", "POST"])
@login_required
def edit_unit(unit_id):

    unit = Unit.query.get(unit_id)
    form = EditUnitForm(request.form)
    

    if not unit:
        abort(403)
    
    form.name.data = unit.name
    form.supply.data = unit.supply
    form.minerals.data = unit.minerals
    form.gas.data = unit.gas
    form.buildtime.data = unit.buildtime


    if request.method == 'POST':
        unit = Unit.query.get(unit_id)
        
        form = EditUnitForm(request.form)
        unit.name = form.name.data
        unit.supply = form.supply.data
        unit.minerals = form.minerals.data
        unit.gas = form.gas.data
        unit.buildtime = form.buildtime.data

        print('dataa: ', unit.name, unit.supply, unit.minerals, unit.gas, unit.buildtime)

        db.session().commit()



        return redirect('units_index')
  
    return render_template("units/edit.html", form = form, unit = unit)

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

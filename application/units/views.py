from application import app, db
from flask import render_template, request, redirect, url_for, abort
from application.units.models import Unit
from application.units.forms import UnitForm
from flask_login import login_required, current_user

# List all units

@app.route("/units", methods=["GET"])
def units_index():
    return render_template("units/list.html", units = Unit.query.all())

# Lists current users units

@app.route("/units/myunits/", methods=["GET"])
@login_required
def units_myindex():
    return render_template("units/list.html", units = Unit.query.filter_by(account_id = current_user.id))


# New unit, redirects to template

@app.route("/units/new/")
@login_required
def units_form():
    return render_template("units/new.html", form = UnitForm())


# Edit unit

@app.route("/units/edit/<unit_id>/", methods=["GET", "POST"])
@login_required
def edit_unit(unit_id):

    if request.method == 'POST':
        

        unit = Unit.query.get(unit_id)
        
        form = UnitForm(request.form)

        if not form.validate():
            return render_template("units/edit.html", form = form, unit = unit)

        unit.name = form.name.data
        unit.supply = form.supply.data
        unit.minerals = form.minerals.data
        unit.gas = form.gas.data
        unit.buildtime = form.buildtime.data

        

        db.session().commit()



        return redirect(url_for("units_index"))

    unit = Unit.query.get(unit_id)
    form = UnitForm(request.form)
    

    if not unit:
        abort(403)
    
    form.name.data = unit.name
    form.supply.data = unit.supply
    form.minerals.data = unit.minerals
    form.gas.data = unit.gas
    form.buildtime.data = unit.buildtime


    
  
    return render_template("units/edit.html", form = form, unit = unit)

# Delete unit

@app.route("/units/delete/<unit_id>/", methods=["GET"])
@login_required
def delete_unit(unit_id):

    unit = Unit.query.get(unit_id)
    db.session.delete(unit)
    db.session().commit()


    return redirect(url_for("units_index"))


# Create unit, returns to index

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

    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("units_index"))

from app import app, db
from models.models import Plant
from flask import render_template, request, redirect


@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")


@app.route("/save-plant", methods=["POST"])
def save_plant():
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(title=name, location=location)
    db.session.add(plant)
    db.session.commit()
    return redirect("/")


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    plant = Plant.query.get(id)
    print(plant.id)
    db.session.delete(plant)
    db.session.commit()
    return redirect("/")


@app.route("/inform-plant/<int:id>")
def inform_plant(id):
    inf_plant = Plant.query.get(id)  # конкретний завод
    print(Plant.title)
    # inf_emploe = Plant.get_by_id_for_flask_empl(id)
    # return render_template("inform-plant.html", inf_plant=inf_plant, inf_emploe=inf_emploe)
    return render_template("inform-plant.html", inf_plant=inf_plant)

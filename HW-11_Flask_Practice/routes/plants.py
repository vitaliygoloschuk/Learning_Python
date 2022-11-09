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

@app.route("/edit-plant/<int:id>")
def edit_plant(id):
    plant = Plant.query.get(id)
    return render_template("add_plant.html", plant=plant)

@app.route("/update-plant/<int:id>", methods = ["POST"])
def update_plant(id):
    plant = Plant.query.get(id)
    plant.title = request.form.get("name")
    plant.location = request.form.get("location")
    db.session.add(plant)
    db.session.commit()
    return redirect("/")

@app.route("/inform-plant/<int:id>")
def inform_plant(id):
    inf_plant = Plant.query.get(id)  # конкретний завод
    print(Plant.title)
    return render_template("inform-plant.html", inf_plant=inf_plant)

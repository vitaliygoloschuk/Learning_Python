from app import app
from models.models import Plant
from flask import render_template, request, redirect


@app.route("/add-plant")
def add_plant():
    return render_template("add_plant.html")


@app.route("/save-plant", methods=["POST"])
def save_plant():
    print(request.form)
    name = request.form.get("name")
    location = request.form.get("location")
    plant = Plant(name, location)
    plant.save()
    return redirect("/")


@app.route("/delete-plant/<int:id>")
def delete_plant(id):
    Plant.delete(id)
    return redirect("/")


@app.route("/inform-plant/<int:id>")
def inform_plant(id):
    inf_plant = Plant.get_by_id_for_flask(id)  # конкретний завод
    inf_emploe = Plant.get_by_id_for_flask_empl(id)
    return render_template("inform-plant.html", inf_plant=inf_plant, inf_emploe=inf_emploe)

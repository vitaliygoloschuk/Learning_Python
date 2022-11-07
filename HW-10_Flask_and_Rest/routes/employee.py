from app import app, db
from models.models import Employee
from flask import render_template, request, redirect


@app.route("/add-employee")
def add_employee():
    return render_template("add_employee.html")


@app.route("/save-employee", methods=["POST"])
def save_employee():
    name = request.form.get("name")
    object_id = request.form.get("object_id")
    type_of_work = request.form.get("type_of_work")
    employee = Employee(name=name, object_id=object_id, type_of_work=type_of_work)
    db.session.add(employee)
    db.session.commit()
    return redirect("/")


# @app.route("/delete-employee/<int:id>")
# def delete_employee(id):
#     employee = Employee.query.get(id)
#     print(employee.id)
#     db.session.delete(employee)
#     db.session.commit()
#     return redirect("/")


# @app.route("/inform-plant/<int:id>")
# def inform_plant(id):
#     inf_plant = Employee.query.get(id)  # конкретний завод
#     # print(Plant.title)
#     # inf_emploe = Plant.get_by_id_for_flask_empl(id)
#     # return render_template("inform-plant.html", inf_plant=inf_plant, inf_emploe=inf_emploe)
#     return render_template("inform-plant.html", inf_plant=inf_plant)

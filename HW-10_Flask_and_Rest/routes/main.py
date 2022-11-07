from app import app
from flask import render_template
from models.models import Plant, Employee


@app.route("/")
def main():
    # plants = Plant.query.order_by(Plant.title.asc()).all()
    # plants = Plant.query.filter(Plant.location == "st. Kyiv 9") #(віддавався лише елемент)
    plants = Plant.query.all()
    # print(plants)
    return render_template("index.html", plants=plants, )

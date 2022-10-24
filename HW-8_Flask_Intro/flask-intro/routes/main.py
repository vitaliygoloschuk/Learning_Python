from app import app


@app.route("/")
def hello():
    return "hello world!!!"


@app.route("/calc/<number>/<number_two>")
def calc(number, number_two):
    result = int(number) + int(number_two)
    return str(result)

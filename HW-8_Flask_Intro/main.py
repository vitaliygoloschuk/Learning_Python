from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hi it's flask app"


@app.route('/calc/{1}')
def calc_one():
    return "1"


@app.route('/calc/2')
def calc_two():
    return "2"


if __name__ == "__main__":
    app.run(debug=True)

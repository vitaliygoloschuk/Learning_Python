
from flask import Flask

app = Flask(__name__)

with app.app_context():
    from routes.main import *


#це той кож який не має імпортуватись в інші файли if __name__ формально в мен записується файлик який виконується


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

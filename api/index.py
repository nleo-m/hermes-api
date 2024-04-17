from flask import Flask
from .routes.transposition.blueprint import transposition
from .routes.hashing.blueprint import hashing

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello world, I'm a working API!"


app.register_blueprint(transposition)
app.register_blueprint(hashing)

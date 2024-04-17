from flask import Flask
from .routes.transposition.blueprint import transposition
from .routes.hashing.blueprint import hashing
from .routes.encoding.blueprint import encoding

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello world, I'm a working API!"


app.register_blueprint(transposition)
app.register_blueprint(hashing)
app.register_blueprint(encoding)

from flask import Flask
from .routes.message.blueprint import message

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello world, I'm a working API!"


app.register_blueprint(message)

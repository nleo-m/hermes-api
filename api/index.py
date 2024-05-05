from flask import Flask, request
from .handlers.main import BHandler

app = Flask(__name__)


@app.route("/", methods=["POST"])
def main():
    handler = BHandler()
    return handler.handle()


if __name__ == "__main__":
    app.run(debug=True)

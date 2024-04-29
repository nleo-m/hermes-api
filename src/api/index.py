from flask import Flask, request
from handlers.main import Handler

app = Flask(__name__)


@app.route("/a", methods=["POST"])
def main():
    handler = Handler()
    return handler.handle()


# if __name__ == "__main__":
#     app.run(debug=True)

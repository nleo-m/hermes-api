from flask import Flask
from routes.message import message_blueprint

app = Flask(__name__)

app.register_blueprint(message_blueprint)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Blueprint, request
from handlers.message_handler import MessageHandler

message_blueprint = Blueprint("message_blueprint", __name__)
handler = MessageHandler()


@message_blueprint.route("/reverse", methods=["POST"])
def reverse_cipher():
    message = request.form["message"]
    return handler.reverse(message)

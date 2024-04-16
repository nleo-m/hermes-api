from .ciphers import *
from flask import Blueprint, request

BASE_PATH = "/message/"
message = Blueprint("message", __name__)


@message.route(BASE_PATH + "reverse", methods=["POST"])
def reverse_handler():
    message = request.form["message"]

    return reverse.cipher(message)

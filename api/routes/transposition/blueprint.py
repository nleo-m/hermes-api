from .ciphers import *
from flask import Blueprint, request

BASE_PATH = "/transposition/"
transposition = Blueprint("transposition", __name__)


@transposition.route(BASE_PATH + "reverse", methods=["POST"])
def reverse_handler():
    transposition = request.form["transposition"]

    return reverse.cipher(transposition)

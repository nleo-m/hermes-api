from .handler import HashHandler as Handler
from flask import Blueprint, request

BASE_PATH = "/hashing/"

hashing = Blueprint("hashing", __name__)
handler = Handler()


@hashing.route(BASE_PATH, methods=["POST"])
def handle():
    return handler.hash(request)

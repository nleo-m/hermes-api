from .handler import EncodeHandler as Handler
from flask import Blueprint, request

BASE_PATH = "/encoding/"

encoding = Blueprint("encoding", __name__)
handler = Handler()


@encoding.route(BASE_PATH, methods=["POST"])
def handle():
    return handler.encode(request)

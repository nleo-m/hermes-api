from flask import request
from .transposer import Transposer
from .encoder import Encoder


class Handler:
    def __init__(self):
        if request:
            self.type = request.json["type"]
            self.setup()

    def handle(self):
        return self.method(self.subject)

    def setup(self):
        self.driver = self.get_driver()
        self.action = request.json.get("action", self.get_default_action_for_driver())
        self.subject = self.get_subject()
        self.method = self.get_method()

    def get_default_action_for_driver(self):
        if isinstance(self.driver, Transposer):
            return "cipher"
        elif isinstance(self.driver, Encoder):
            return "encode"

    def get_driver(self):
        if self.type == "transposition":
            return Transposer()
        if self.type == "encoding":
            return Encoder()

    def get_method(self):
        return self.method_is_supported()

    def method_is_supported(self):
        req_method = request.json["method"]
        method = getattr(self.driver, f"{req_method}_{self.action}", None)

        if callable(method):
            return method

    def get_subject(self):
        if self.subject_is_a_file():
            return request.files["subject"].read()

        return request.json["subject"].encode("utf-8")

    def subject_is_a_file(self):
        if request.json.get("subject"):
            return False

        return True

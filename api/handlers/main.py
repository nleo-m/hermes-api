from flask import request, send_file
import io

from .transposer import Transposer
from .encoder import Encoder
from .hasher import Hasher
from .encrypter import Encrypter


class Handler:
    def __init__(self):
        if request:
            self.setup()

    def setup(self):
        self.supported_actions_and_drivers = {
            "transpose": Transposer,
            "detranspose": Transposer,
            "encode": Encoder,
            "decode": Encoder,
            "encrypt": Encrypter,
            "decrypt": Encrypter,
            "hash": Hasher,
        }
        self.file_subject = False
        self.action = self.get_action()
        self.driver = self.get_driver()
        self.subject = self.get_subject()
        self.method = self.get_method()

    def handle(self):
        ciphered_data = self.method(self.subject)

        if self.file_subject:
            return self.return_file(ciphered_data)

        return ciphered_data

    def return_file(self, data):
        filename = request.files["subject"].filename
        file = io.BytesIO(data)
        return send_file(file, download_name=filename, as_attachment=True)

    def get_action(self):
        if self.action_is_supported():
            return request.form["action"]

    def action_is_supported(self):
        if request.form["action"] not in self.supported_actions_and_drivers.keys():
            return False

        return True

    def get_driver(self):
        driver = self.supported_actions_and_drivers.get(self.action)
        return driver()

    def get_method(self):
        return self.method_is_supported()

    def method_is_supported(self):
        req_method = request.form["method"]
        method = getattr(self.driver, f"{req_method}_{self.action}", None)

        if callable(method):
            return method

    def get_subject(self):
        if self.subject_is_a_file():
            self.file_subject = True
            return request.files["subject"].read()

        return request.form["subject"].encode("utf-8")

    def subject_is_a_file(self):
        if request.form.get("subject"):
            return False

        return True

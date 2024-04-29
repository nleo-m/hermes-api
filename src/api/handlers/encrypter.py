from cryptography.fernet import Fernet
from decouple import config
from flask import request


class Encrypter:
    def __init__(self):
        self.fernet = self.get_fernet()

    def get_fernet(self):
        if request.form.get("key", None):
            return Fernet(request.form["key"])

        return Fernet(config("FERNET_KEY"))

    def fernet_encrypt(self, subject):
        return self.fernet.encrypt(subject)

    def fernet_decrypt(self, subject):
        return self.fernet.decrypt(subject)

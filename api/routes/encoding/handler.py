import base64
import urllib


class EncodeHandler:
    def encode(self, request):
        subject = self.get_subject(request)
        method = request.form["method"]

        if method == "base64":
            return base64(subject)

        if method == "url":
            return urllib.parse.quote(subject)

        return "Please provide a valid encoding method method!"

    def get_subject(self, request):
        return request.form["subject"].encode("utf-8")

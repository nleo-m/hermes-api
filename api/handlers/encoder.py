import urllib
import base64


class Encoder:
    def url_encode(self, string):
        return urllib.parse.quote(string)

    def url_decode(self, string):
        return urllib.parse.unquote(string)

    def base64_encode(self, string):
        return base64.b64encode(string)

    def base64_decode(self, string):
        return base64.b64decode(string)

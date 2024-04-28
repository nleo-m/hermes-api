import urllib


class Encoder:
    def url_encode(self, string):
        return urllib.parse.quote(string)

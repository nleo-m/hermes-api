import hashlib


class Hasher:
    def md5_hash(self, subject):
        return hashlib.md5(subject).hexdigest()

    def sha1_hash(self, subject):
        return hashlib.sha1(subject).hexdigest()

    def sha256_hash(self, subject):
        return hashlib.sha256(subject).hexdigest()

    def sha512_hash(self, subject):
        return hashlib.sha512(subject).hexdigest()

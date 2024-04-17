import hashlib


class HashHandler:
    def hash(self, request):
        subject = self.get_subject(request)
        method = request.form["method"]

        if method == "md5":
            return hashlib.md5(subject).hexdigest()

        if method == "sha1":
            return hashlib.sha1(subject).hexdigest()

        if method == "sha224":
            return hashlib.sha224(subject).hexdigest()

        if method == "sha256":
            return hashlib.sha256(subject).hexdigest()

        if method == "sha384":
            return hashlib.sha384(subject).hexdigest()

        if method == "sha512":
            return hashlib.sha512(subject).hexdigest()

        if method == "scrypt":
            return hashlib.scrypt(subject).hexdigest()

        return "Please provide a valid hash method!"

    def get_subject(self, request):
        if self.subject_is_a_file(request):
            return request.files["subject"].read()

        return request.form["subject"].encode("utf-8")

    def subject_is_a_file(self, subject):
        if subject.form.get("subject"):
            return False

        return True

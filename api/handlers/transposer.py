class Transposer:
    def reverse_cipher(self, value):
        return value[::-1]

    def reverse_decipher(self, value):
        return self.reverse_cipher(value)

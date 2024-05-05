class Transposer:
    def reverse_transpose(self, string):
        return string[::-1]

    def reverse_detranspose(self, string):
        return self.reverse_transpose(string)

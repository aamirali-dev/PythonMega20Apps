import random


class CreditCard:
    def __init__(self):
        self._number = []

    def generate(self):
        self._number = [random.randrange(1000, 9999) for _ in range(4)]

    @property
    def number(self):
        return " ".join(self._number)


class VisaMixin(CreditCard):
    def generate(self):
        super().generate()
        self._number[0] = 4200 + (self._number[0] % 100)


class MasterCardMixin(CreditCard):
    def generate(self):
        super().generate()
        self._number[0] = 5300 + (self._number[0] % 100)


class ValidMixin(CreditCard):
    def generate(self):
        super().generate()
        self._checksum()

    def _checksum(self):
        self.checksum = 10


class Visa(VisaMixin, CreditCard):
    pass



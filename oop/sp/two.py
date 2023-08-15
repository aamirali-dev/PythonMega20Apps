import random
import string


class PasswordGenerator:

    _input_universe = {
        'letters': list(string.ascii_letters),
        'numbers': [str(i) for i in range(10)],
        'punctuation': list(string.punctuation),
    }

    def __init__(self, strength='mid', length=None):
        self.strength = strength
        if length is not None:
            self.length = length
        else:
            if strength == 'low':
                length = 8
            elif strength == 'high':
                length = 32
            else:
                length = 16
        self._generate()

    @staticmethod
    def show_input_universe():
        return PasswordGenerator._input_universe

    def _generate(self):
        population = self._input_universe['letters']
        if self.strength=='high':
            population += self._input_universe['numbers'] + self._input_universe['punctuation']
        # print(random.choices(population, self.length))

        self.password = "".join(random.choices(population, k=self.length))


print(PasswordGenerator('high', 23).password)

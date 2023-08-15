import math

from IPython.core.display import Math
from functools import total_ordering


@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        return False

    def __bool__(self):
        if abs(self)==0:
            return False
        return True

    def __le__(self, other):
        if abs(self) < abs(other):
            return True
        return False

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'X', 'y', 'Y', 'z', 'Z']:
            return eval(f'self.{item.lower()}')
        return NotImplemented




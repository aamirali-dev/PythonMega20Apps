class Point3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class ColoredPoint(Point3D):
    __slots__ = 'color'

    def __init__(self, x, y, z, color='black'):
        super().__init__(x, y, z)
        self.color = color


class ShapedPoint(Point3D):
    __slots__ = 'shape'

    def __init__(self, x, y, z, shape='sphere'):
        super().__init__(x, y, z)
        self.shape = shape


p = Point3D(1, 2, 3)
cp = ColoredPoint(1, 2, 3, 'red')
sp = ShapedPoint(1, 2, 3, 'cube')

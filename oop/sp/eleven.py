class IntDescriptor:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.get_key())

    def __set__(self, instance, value):
        if not  isinstance(value, int):
            raise TypeError(f'{self.name} must be of type int')
        if self.min_value <= value <= self.max_value:
            instance.__dict__[self.get_key()] = value
        else:
            raise ValueError(f'{self.name} must be greater then {self.min_value} and less then {self.max_value}')

    def __delete__(self, instance):
        del instance.__dict__[self.get_key()]

    def get_key(self):
        return f'int_descriptor_{self.name}'


class StudentProfile:
    gre_score = IntDescriptor(min_value=130, max_value=340)
    sat_score = IntDescriptor(min_value=400, max_value=1600)

    def __init__(self, name, gre_score=130, sat_score=400):
        self.name = name
        self.gre_score = gre_score
        self.sat_score = sat_score

    def __repr__(self):
        return f'StudentProfile(name=\'{self.name}\', gre_score={self.gre_score}, sat_score={self.sat_score})'


sp = StudentProfile('Andrew', sat_score=1200, gre_score=130)
print(sp)
# sp.gre_score=3000

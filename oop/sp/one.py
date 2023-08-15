import random


class Student:
    educational_platform = 'udemy'
    _GREETINGS = [
        'Hi, I\'m {0}',
        'Hey there, my name is {0}',
        'Hi. Oh, my name is {0}',
    ]

    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def greet(self):
        return self._GREETINGS[random.randint(0,2)].format(self.name)


names = ['Ali', 'Hamza', 'Arif', 'Razi', 'Momin']
for name in names:
    s = Student(name)
    print(s.greet())

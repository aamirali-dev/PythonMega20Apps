from enum import Flag, auto


class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


class Permissions:
    def __init__(self, *permissions):
        self._permissions = Permission(0)
        for permission in permissions:
            self._permissions |= permission

    def __add__(self, other):
        if isinstance(other, Permission):
            self._permissions |= other
            return  self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Permission):
            self._permissions & (~other)
            return self
        return NotImplemented

    def __contains__(self, item):
        if isinstance(item, Permission):
            return self._permissions & item

    def __repr__(self):
        return repr(self._permissions)


class FileManager:
    def is_allowed_to(self, permission):
        return True

    def read(self, file):
        if self.is_allowed_to(Permission.READ):
            print(f"Reading {file}")
        else:
            print('user do not have permission to read')

    def write(self, file, content):
        if self.is_allowed_to(Permission.WRITE):
            print(f"Writing {content} to {file}")
        else:
            print('user do not have permission to write')

    def execute(self, file):
        if self.is_allowed_to(Permission.EXECUTE):
            print(f"Executing {file}")
        else:
            print('user do not have permission to execute')


class User(FileManager):
    _DEFAULT_PERMISSIONS = {
        'admin': Permissions(Permission.READ, Permission.WRITE, Permission.EXECUTE),
        'user': Permissions(Permission.READ),
        'manager': Permissions(Permission.READ, Permission.WRITE),
        'support': Permission(Permission.EXECUTE),
    }

    def __init__(self, name, user_role):
        self.name = name
        self.role = user_role
        self.permissions = self._DEFAULT_PERMISSIONS[user_role]

    def is_allowed_to(self, permission):
        if permission in self.permissions:
            return True
        return False

    def __repr__(self):
        return f'User(name={self.name}, user_role={self.role})'

    # @staticmethod
    # def _to_role(role):
    #     roles = ['']


u1 = User('Aeron', 'user')
u2 = User('Andrew', 'admin')
print(u1.permissions)
print(u2.permissions)
u2.write('script.py', 'for i in range(10): print(i)')
u1.read('script.py')
u1.execute('script.py')


from collections import UserDict


class BidirectionalDict(UserDict):
    def __getitem__(self, item):
        if item in self:
            return super().__getitem__(item)
        if item in self.values():
            for (key, value) in self.items():
                if value == item:
                    return key
        raise KeyError(f"{item} is neither a key, nor a value")


bd = BidirectionalDict({'code': 'more', 'sleep': 'less'})
print(bd)
print(bd['code'])
print(bd['more'])
bd.update([('sleep', 'deeper')])
print(bd['sleep'])
print(bd['deeper'])


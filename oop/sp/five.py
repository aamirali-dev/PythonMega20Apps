class DNABase:

    _VALID_BASES = {
        'a' : 'adenine',
        'c' : 'cytosine',
        'g' : 'guanine',
        't' : 'thymine',
    }

    def __init__(self, nucleotide):
        self.base = nucleotide

    def get_base(self):
        return self._base

    def set_base(self, nucleotide):
        ntide = nucleotide.lower()
        if ntide in self._VALID_BASES.keys():
            self._base = self._VALID_BASES[ntide]
        elif ntide in self._VALID_BASES.values():
            self._base = ntide
        else:
            raise ValueError(f'{nucleotide} is not a valid base')

    def __repr__(self):
        return f'DNABase(nucleotide={self.base})'

    base = property(fget=get_base, fset=set_base)


base = DNABase('A')
print(repr(base))
base.base = 'ThyMIne'
print(repr(base))

class Contact:
    def __init__(self, name, last_name, phone=None, email=None, display_mode='regular'):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode

    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        if self.phone is not None and other.phone is not None:
            return self.phone == other.phone
        if self.email is not None and other.email is not None:
            return self.email == other.email
        return self.name == other.name and self.last_name == other.last_name

    def __str__(self):
        return self.last_name[0] + self.name[0]

    def __repr__(self):
        return 'Contact(name={0}, last_name={1})'.format(
            self.name[:2] + '*'*len(self.name),
            self.last_name[0] + '*'*len(self.last_name))

    def __format__(self, format_spec):
        if format_spec == 'unmasked':
            return f'Contact(name={self.name}, last_name={self.last_name}, phone={self.phone}, email={self.email})'

        if self.display_mode == 'masked':
            return repr(self)

    def __hash__(self):
        return hash((self.name, self.last_name, self.phone, self.email))


c1 = Contact('Andy', 'Paulo')
c2 = Contact('Andy', 'Paulo', '02302832323')
c3 = Contact('Andy', 'Paulo', '02302832323', 'andy.paulo@curemd.com')
c4 = Contact('Andy', 'Paulo', '02302832323', 'andy.paulo@curemd.com', display_mode='masked')

if c1 == c2:
    print(True)
print(repr(c1))
print(str(c2))
print("{c:unmasked}".format(c=c4))

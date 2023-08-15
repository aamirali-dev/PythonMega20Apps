class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError(f'amount can\'t be less then 0')
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError(f'amount can\'t be less then 0')
        if amount > self.balance:
            raise ValueError(f'amount must be less then balance. balance is {self.balance}')
        self._balance -= amount

    def __repr__(self):
        return f'A {self.__class__.__name__} with ${self.balance} in it'


class SavingsBankAccount(BankAccount):
    def pay_interest(self):
        self.deposit(self.balance * self.get_interest())

    def get_interest(self):
        return 0.0035


class HighInterestBankAccount(SavingsBankAccount):
    def __init__(self, balance=0, withdrawal_fee=0):
        super().__init__(balance)
        self._withdrawal_fee = withdrawal_fee

    @property
    def withdrawal_fee(self):
        return self._withdrawal_fee

    def get_interest(self):
        return 0.007

    def withdraw(self, amount):
        super().withdraw(amount + self.withdrawal_fee)


class LockedInBankAccount(HighInterestBankAccount):
    def get_interest(self):
        return 0.009

    def withdraw(self, amount):
        raise PermissionError('early withdrawal is not allowed from LockedIn Bank Account')


b = BankAccount(initial_balance=100)
print(repr(b))
b.deposit(2)
b.withdraw(70)
print(repr(b))
sb = SavingsBankAccount(initial_balance=140)
print(repr(sb))
sb.pay_interest()
print(repr(sb))
hiba = HighInterestBankAccount(withdrawal_fee=5)
hiba.deposit(140)
hiba.pay_interest()
print(repr(hiba))
hiba.withdraw(0.98)
print(repr(hiba))
liba = LockedInBankAccount(1000)
print(repr(liba))
liba.pay_interest()
print(repr(liba))
liba.withdraw(20)

from decimal import *


class Account(object):
    _qb = Decimal('0.00')  # class constant, accessible without creating an instance.

    def __init__(self, name: str, opening_balance: float = 0.0):
        self.name = name
        self._balance = Decimal(opening_balance).quantize(Account._qb)
        print("Account created for {}. ".format(self.name), end='')
        self.show_balance()

    def deposit(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if decimal_amount > Account._qb:
            self._balance = self._balance + decimal_amount
            print("{} deposited".format(decimal_amount))
        return self._balance

    def withdraw(self, amount: float) -> Decimal:
        decimal_amount = Decimal(amount).quantize(Account._qb)
        if Account._qb < decimal_amount <= self._balance:
            self._balance = self._balance - decimal_amount
            print("{} withdrawn".format(decimal_amount))
            return decimal_amount
        else:
            print("The amount must be greater than zero and no more than your account balance")
            return Account._qb

    def show_balance(self):
        print("Balance on account {} is {}".format(self.name, self._balance))


if __name__ == '__main__':
    tim = Account("Tim")
    tim.deposit(10.1)
    tim.deposit(0.1)
    tim.deposit(0.1)
    tim.withdraw(0.3)
    tim.withdraw(0)
    tim.show_balance()

    print("=" * 80)
    x = tim.withdraw(900)
    print(x)

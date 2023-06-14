from typeguard import typechecked
import random


@typechecked
class NegativeMoney(Exception):
    def __init__(self, balance_positive):
        super().__init__("El saldo de la cuenta no puede ser negativo")
        self.balance = balance_positive


class TakenGreaterThanMoneyAccount(Exception):
    def __init__(self, money_retired):
        super().__init__("El dinero retirado no puede ser más que el saldo de la cuenta bancaria")
        self.money = money_retired


class BankAccount:

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise NegativeMoney(balance)
        self.__number_account = random.randrange(1, 9999999999)
        self.__balance = balance

    def __str__(self):
        return f'Número de cta: {self.__number_account:010d} Saldo: {self.__balance:0.2f} €'

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def deposit(self, money: int):
        self.__balance += money

    def withdraw(self, money: int):
        if self.__balance < 0 and self.__balance < money:
            raise TakenGreaterThanMoneyAccount(money)
        else:
            self.__balance -= money

    def transfer(self, other: 'BankAccount', money: int):
        self.withdraw(money)
        other.deposit(money)


if __name__ == '__main__':
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    try:
        cuenta1.deposit(-2000)
        cuenta2.withdraw(600)
        cuenta3.deposit(75)
        cuenta1.withdraw(55)
        cuenta2.transfer(cuenta3, 100)
    except (TakenGreaterThanMoneyAccount, NegativeMoney) as e:
        print(f'Error: {e}')
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

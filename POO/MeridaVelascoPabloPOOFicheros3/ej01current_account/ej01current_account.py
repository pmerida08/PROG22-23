"""
1. Modifica el ejercicio de la cuenta corriente para que el método que almacena en un fichero el estado del objeto
guarde el objeto entero y el que lo recupera lo restaure. En esta versión no le pasamos nombre de fichero al método a
la hora de guardarlo, usará el número de cuenta corriente para ello.

"""

from typeguard import typechecked
import random
import pickle


class BankNegativeMoneyError(Exception):
    def __init__(self):
        super().__init__('El dinero de una cuenta no puede ser negativo')


class BankTakenGreaterThanMoneyAccountError(Exception):
    def __init__(self):
        super().__init__('El dinero retirado no puede ser más que el saldo de la cuenta bancaria')


@typechecked
class BankAccount:

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise BankNegativeMoneyError()
        self.__number_account = random.randrange(1, 9999999999)
        self.__balance = balance

    def __str__(self):
        return f'Número de cta: {self.__number_account:010d} Saldo: {self.__balance:0.2f} €'

    def __repr__(self):
        return f"{self.__class__.__name__}"

    @property
    def number_account(self):
        return self.__number_account

    def deposit(self, money: int):
        self.__balance += money

    def withdraw(self, money: int):
        if self.__balance < 0 and self.__balance < money:
            raise BankTakenGreaterThanMoneyAccountError()
        else:
            self.__balance -= money

    def transfer(self, other: 'BankAccount', money: int):
        self.withdraw(money)
        other.deposit(money)

    def save_account(self):
        file_name = f"account_{self.__number_account}.pickle"
        with open(file_name, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def restore_account(number_account):
        file_name = f"account_{number_account}.pickle"
        try:
            with open(file_name, 'rb') as file:
                account = pickle.load(file)
                return account
        except FileNotFoundError:
            print("Error: No se encontró la cuenta bancaria.")
            return None


if __name__ == '__main__':
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)
    try:
        cuenta1.deposit(2000)
        cuenta2.withdraw(600)
        cuenta3.deposit(75)
        cuenta1.withdraw(55)
        cuenta2.transfer(cuenta3, 100)
    except (BankTakenGreaterThanMoneyAccountError, BankNegativeMoneyError) as e:
        print(f'Error: {e}')
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

    cuenta1.save_account()
    cuenta2.save_account()
    cuenta3.save_account()

    restored_account = BankAccount.restore_account(cuenta1.number_account)
    if restored_account:
        print("Cuenta bancaria restaurada:")
        print(restored_account)

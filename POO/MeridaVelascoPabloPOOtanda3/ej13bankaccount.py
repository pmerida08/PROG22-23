"""
13. Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta
se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta.
La cuenta se puede generar con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente. En una
cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra. No se
permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de este, en el que se pide
llevar un registro de los movimientos realizados.

Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)

Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 05/03/2023
"""
from typeguard import typechecked
import random

@typechecked
class BankAccount:

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise ValueError('El dinero de una cuenta no puede ser negativo')
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
            raise ValueError('El dinero retirado no puede ser más que el saldo de la cuenta bancaria')
        else: self.__balance -= money

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
    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)
    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

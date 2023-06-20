"""
        Ejercicio 3:

            Modifica el ejercicio de POO que gestiona una cuenta bancaria con movimientos, de forma que añadas a la
            clase un método para guardar todos los datos de la cuenta bancaria (número, saldo y movimientos) en un
            fichero elegido por el cliente, y un nuevo constructor que reciba como parámetro un fichero como el anterior
            y cree el objeto con esos datos. Pruébalo con un programa.

            P.D.- Usa excepciones para controlar el manejo de ficheros y en caso de no poder operar dar el mensaje de
            error correspondiente.

"""
import pickle

from typeguard import typechecked
import random


class BankAccountError(Exception):

    def __init__(self, msg):
        super().__init__(f"Error: {msg}")
        self.msg = msg


class BankNegativeBalanceError(BankAccountError):

    def __init__(self, balance):
        super().__init__(f"El saldo tiene que ser positivo. Recibido: {balance}")
        self.balance = balance


class BankNegativeAmountError(BankAccountError):

    def __init__(self, amount):
        super().__init__(f"La cantidad no puede ser negativa. Recibido: {amount}")
        self.amount = amount


@typechecked
class BankAccount:
    __registered_accounts = []

    def __init__(self, balance: int = 0):
        if balance < 0:
            raise BankNegativeBalanceError("El saldo no puede ser negativo")
        while True:
            number_account = random.randint(1, 9999999999)
            if number_account not in BankAccount.__registered_accounts:
                BankAccount.__registered_accounts.append(number_account)
                self.__account = number_account
                break
        self.__balance = balance
        self.__movements_list = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            raise BankNegativeAmountError(amount)
        self.__balance += amount
        self.__movements_list.append(f"Ingreso de {amount:.2f} €. Saldo: {self.__balance:.2f} €")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("El dinero a sumar no puede ser positivo")
        if amount > self.__balance:
            raise ValueError("No puedes quitar mas dinero del que tienes en la cuenta")
        self.__balance -= amount
        self.__movements_list.append(f"Cargo de {amount:.2f} €. Saldo: {self.__balance:.2f} €")

    def transfer(self, other: 'BankAccount', money):
        self.__balance -= money
        self.__movements_list.append(f"Transferencia de {money} € de la cuenta {self.__account} a la cuenta"
            f"{other.__account}. Saldo: {self.__balance}")
        other.__balance += money
        self.__movements_list.append(f"Transferencia de {money} € de la cuenta {other.__account} a la cuenta"
            f"{self.__account}. Saldo: {other.__balance}")

    def save_file(self):
        filename = str(self.__account)
        with open(filename + ".pkl", "wb") as f:
            pickle.dump(self, f)

    def movements(self):
        str_ = ""
        for m in self.__movements_list:
            str_ += f"{m} \n"
        return str_

    def __str__(self):
        return f"Número de cta: {self.__account} Saldo: {self.__balance:.2f} €"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__balance})"


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
    cuenta1.save_file()
    cuenta2.save_file()
    cuenta3.save_file()
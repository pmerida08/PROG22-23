"""
Vamos a crear la clase CashRegister que simula el comportamiento de una caja registradora
como la que tiene cualquier comercio. Nuestra caja tendrá las siguientes operaciones:

- Entrada y salida de efectivo. Tenemos que registrar la cantidad que entra o sale, la fecha y hora
de la operación y el concepto. Esta operación tiene un identificador numérico que se genera
automáticamente y por defecto es el de la operación anterior incrementado en 1. No se puede añadir
un movimiento con fecha y hora anterior al último. Si la fecha y hora no se indica se toma la actual.

- Borrado del último movimiento. El resto de movimientos no se pueden borrar porque
descuadrarían los saldos de la caja.

- Obtención de los movimientos de la caja.

Esta clase tiene que tener, al menos, los siguientes métodos:

• add()
    ◦ recibe la cantidad (positiva o negativa), el concepto y la fecha y hora (datetime)
    ◦ lanza excepción si la fecha y hora del movimiento es anterior al último
    ◦ lanza excepción si el saldo que resulte después de aplicar este movimiento es negativo
    ◦ si fecha y hora no se indican se toma la actual
• delete_last()
    ◦ borra el último movimiento
• __str_ )₍
    ◦ devuelve una cadena con todos los movimientos y su saldo al final, si se imprime tiene que ser visualmente aceptable.
• balance()
    ◦ devuelve el saldo de la caja


"""
from typeguard import typechecked
from movement import Movement as Move
from datetime import datetime

@typechecked
class CashRegister:

    def __init__(self):
        self.__registered = []
        self.__balance = 0

    def add(self, amount: float, concept: str, date_time= datetime.now()):
        m = Move(amount=amount, concept=concept, date_time=date_time)
        self.__registered.append(m)
        self.__balance += m.amount
        if amount < 0:
            print(f'Has cogido de la caja registradora: {abs(m.amount)} €')
        else:
            print(f'Has añadido de la caja registradora: {m.amount} €')
        print(f'Ahora la caja registradora tiene: {self.__balance:.2f} €')

    def delete_last(self):
        move_deleted = self.__registered[-1]
        self.__balance -= move_deleted.amount
        self.__registered.pop()

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
            print()
            print(f"{self.__class__.__name__}:")
            for i in range(len(self.__registered)):
                print(f'{self.__registered[i]}')
            return ''

    @balance.setter
    def balance(self, value):
        self.__balance = value

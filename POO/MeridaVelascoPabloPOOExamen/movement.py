"""
Los movimientos de caja se guardarán en una lista y serán objetos de la clase Movement. Esta
clase tendrá los siguientes atributos:
• last_number (de clase)
    ◦ último número de movimiento asignado, cambiará al crear otro
• number
    ◦ identificador numérico del movimiento, será el último asignado incrementado en 1
• date_time
    ◦ fecha y hora del movimiento
• amount
    ◦ importe del movimiento, será positivo si es una entrada y negativo en caso contrario
• concept
    ◦ concepto asignado al movimiento
Los objetos de esta clase serán inmutables, pero el atributo de clase last_number es modificable.

"""
from typeguard import typechecked
from datetime import datetime

@typechecked
class Movement:

    last_number = 1

    def __init__(self, amount: float, concept:str ,date_time: datetime.now()):
        self.__date_time = date_time
        self.__amount = amount
        self.__concept = concept
        self.__number = 0
        self.__number += Movement.last_number
        Movement.last_number += 1

    @property
    def date_time(self):
        return self.__date_time


    @property
    def amount(self):
        return self.__amount


    @property
    def number(self):
        return self.__number


    @property
    def concept(self):
        return self.__concept

    def __str__(self):
        return f'Número: {self.__number}, Cantidad: {self.__amount}, Concepto: {self.concept}, Fecha: {self.date_time.date()}, Hora: {self.date_time.time()}'

"""
11. Implementa la clase Terminal. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar
unos a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa
principal que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que validarse
como tales al crear el objeto (solo dígitos, empiezan por 9, 6 o 7, su longitud es de nueve dígitos) y no puede haber
dos terminales con el mismo número.

Programa principal:

t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)

Salida:

No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 03/03/2023

"""

from typeguard import typechecked

@typechecked
class Terminal:
    __LENGTH_PHONE_NUMBER = 9

    def __init__(self, number: str):
        __registered_numbers = []
        if len(number) == Terminal.__LENGTH_PHONE_NUMBER and number[0] in '967' and number not in __registered_numbers:
            self.__phone_number = number
            self.__talk_seconds = 0
            __registered_numbers.append(number)
        else: raise ValueError('El formato del número de teléfono es inválido.')

    def call(self, tel: 'Terminal', seconds: int):
        if seconds < 0:
            raise ValueError('El tiempo de llamada no puede ser negativo.')
        tel.__talk_seconds += seconds
        self.__talk_seconds += seconds
        return f'{self} acaba de llamar {tel} por {seconds}s de conversación.'

    @property
    def talk_seconds(self):
        return self.__talk_seconds

    def __repr__(self):
            return f'{self.__class__.__name__}'

    def __str__(self):
        return f'Nº {self.__phone_number[:3]} {self.__phone_number[3:5]} {self.__phone_number[5:7]} {self.__phone_number[7:9]} - {self.__talk_seconds}s de conversación'

if __name__ == '__main__':
    t1 = Terminal("678112233")
    t2 = Terminal("644744469")
    t3 = Terminal("622328909")
    t4 = Terminal("664739818")
    print(t1)
    print(t2)
    t1.call(t2, 320)
    t1.call(t3, 200)
    print(t1)
    print(t2)
    print(t3)
    print(t4)
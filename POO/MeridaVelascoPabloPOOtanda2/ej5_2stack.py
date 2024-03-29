"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otro tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    Generar la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    Obtener el número de elementos almacenados (tamaño).
    Saber si la pila o la cola está vacía.
    Vaciar completamente la pila o la cola.

    Para el caso de la pila:
        Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
        Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
        Leer el elemento superior de la pila sin retirarlo (top).

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 15/01/2023

"""
from typeguard import typechecked


@typechecked
class Stack:

    def __init__(self, *elements):
        self.__elements = list(elements)

    @classmethod
    def from_stack(cls, other: 'Stack'):
        new_stack = cls()
        new_stack.__elements = list(other.__elements)
        return new_stack

    def __repr__(self):
        return f"{self.__class__.__name__}(values = {self.__elements})"

    @property
    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return len(self.__elements) == 0

    def clear(self):
        self.__elements.clear()

    def push(self, value):
        self.__elements.insert(-1, value)

    def top(self):
        return self.__elements[0]

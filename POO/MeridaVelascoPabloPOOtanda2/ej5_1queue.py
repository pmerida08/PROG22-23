"""
5. Crea una clase que represente una estructura de datos tipo pila (stack) y otro tipo cola (queue).

La pila y la cola permitirán estas operaciones:

    Generar la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
    Obtener el número de elementos almacenados (tamaño).
    Saber si la pila o la cola está vacía.
    Vaciar completamente la pila o la cola.

    Para el caso de la cola:
        Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
        Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
        Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 15/01/2023

"""

class Queue:

    def __init__(self, *elements):
        self.__elements = list(elements)

    @classmethod
    def from_queue(cls, other: 'Queue'):
        new_queue = cls()
        new_queue.__elements = list(other.__elements)
        return new_queue

    def __repr__(self):
        return f"{self.__class__.__name__}(values = {self.__elements})"

    @property
    def size(self):
        return len(self.__elements)

    def is_empty(self):
        return len(self.__elements) == 0

    def clear(self):
        self.__elements.clear()

    def enqueue(self, value):
        self.__elements.append(value)

    def dequeu(self):
        return self.__elements.pop(0)

    def front(self):
        return self.__elements[0]

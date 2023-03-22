"""
2 Implementa una clase Point con sus atributos x e y. La clase debe contener: su constructor, los getters y
setters, un invertCoordinates() que invierta las coordenadas x e y del punto. Además, la clase debe tener un
toString() para poder imprimir los puntos en formato “(x, y)”. Implementa un clase tester PointTester con un método
main() donde crees un punto, lo imprimas utilizando de manera implícita el toString(), imprimas su coordenada x,
asignes 0 a su coordenada x, y vuelvas a imprimir el punto.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 15/01/2023
"""
from typeguard import typechecked

class Point:

    @typechecked # check del tipado de las variables
    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    @property # getter de la coordenada X (Devuelve el valor de X)
    def x(self):
        return self.__x

    @property
    def y(self): # getter de la coordenada Y (Devuelve el valor de Y)
        return self.__y

    def invert_coordinates(self):
        aux = self.__x
        self.__x = self.__y
        self.__y = aux

    def __str__(self):
        return f'La posición del punto es {self.__x, self.__y}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__x}, {self.__y})'

    @y.setter
    @typechecked
    def y(self, value: int):
        self.__y = value

    @x.setter
    @typechecked
    def x(self, value: int):
        self.__x = value

"""
3. Implementa la clase Rectangulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos
puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 15/01/2023
"""
from ej02point import Point
from typeguard import typechecked

@typechecked
class Rectangle:

    def __init__(self, point1: Point, point2: Point):
        self.point1, self.point2 = point1, point2

    @property
    def point1(self):
        return self.__point1

    @point1.setter
    def point1(self, value: Point):
        self.__point1 = value

    @property
    def point2(self):
        return self.__point2

    @point2.setter
    def point2(self, value: Point):
        self.__point2 = value

    @property
    def calc_area(self):
        return abs((self.point1.x - self.point2.x) * (self.point1.y - self.point2.y))

    @property
    def calc_perimeter(self):
        return 2 * abs(self.point1.x - self.point2.x) + 2 * abs(self.point1.y - self.point2.y)

    def __str__(self):
        return f'El perímetro del rectángulo es de {self.calc_perimeter},' \
            f' y el área es de: {self.calc_area}'

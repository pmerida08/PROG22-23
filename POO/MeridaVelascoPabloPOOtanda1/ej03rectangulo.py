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


class Rectangle:

    @typechecked
    def __init__(self, point1: Point, point2: Point):
        self.point_x = point1
        self.point_y = point2

    @property
    def point_x(self):
        return self.__point1

    @property
    def point_y(self):
        return self.__point2

    @point_x.setter
    def point_x(self, value: Point):
        self.__point1 = value

    @point_y.setter
    def point_y(self, value: Point):
        self.__point2 = value

    @property
    def calc_area(self):
        return abs((self.point_x.x - self.point_y.x) * (self.point_x.y - self.point_y.y))

    @property
    def calc_perimeter(self):
        return 2 * abs(self.point_x.x - self.point_y.x) + 2 * abs(self.point_x.y - self.point_y.y)

    def __str__(self):
        return f'El perímetro del rectángulo es de {self.calc_perimeter},' \
               f' y el área es de: {self.calc_area}'

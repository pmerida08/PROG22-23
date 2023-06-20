"""
7. Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos
hacer las siguientes operaciones:

    - Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye
    simplificada, no se puede dividir por cero.
    - Obtener resultado de la fracción (número real).
    - Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
    - Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
"""
from typeguard import typechecked
import math


@typechecked
class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError('El denominador no puede ser 0.')

        mcd = math.gcd(numerator, denominator)

        self.__numerator = numerator // mcd
        self.__denominator = denominator // mcd

    @property
    def numerator(self):
        return self.__numerator

    @property
    def denominator(self):
        return self.__denominator

    @property
    def result(self):
        return self.numerator / self.denominator

    def __add__(self, other):
        mcm = (self.denominator * other.denominator)
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator // mcm + other.numerator // mcm, denominator=mcm)
        return Fraction(numerator=self.numerator // mcm + other // mcm, denominator=mcm)

    def __sub__(self, other):
        mcm = (self.numerator * self.denominator) // math.gcd(self.numerator, self.denominator)
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator // mcm - other.numerator // mcm, denominator=mcm)
        return Fraction(numerator=self.numerator // mcm - other // mcm, denominator=mcm)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator * other.numerator,
                            denominator=self.denominator * other.denominator)
        return Fraction(numerator=self.numerator * other, denominator=self.denominator)

    def __rmul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator * other.numerator,
                            denominator=self.denominator * other.denominator)
        return Fraction(numerator=self.numerator * other, denominator=self.denominator)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerator * other.denominator,
                            denominator=self.denominator * other.numerator)
        return Fraction(numerator=self.numerator, denominator=self.denominator * other)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__numerator} / {self.__denominator}"

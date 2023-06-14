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

        self.__numerador = numerator // mcd
        self.__denominador = denominator // mcd

    @property
    def numerador(self):
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    @property
    def result(self):
        return self.numerador / self.denominador

    def __add__(self, other):
        mcm = (self.denominador * other.denominador)
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerador // mcm + other.numerador // mcm, denominator=mcm)
        return Fraction(numerator=self.numerador // mcm + other // mcm, denominator=mcm)

    def __sub__(self, other):
        mcm = (self.numerador * self.denominador) // math.gcd(self.numerador, self.denominador)
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerador // mcm - other.numerador // mcm, denominator=mcm)
        return Fraction(numerator=self.numerador // mcm - other // mcm, denominator=mcm)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerador * other.numerador,
                            denominator=self.denominador * other.denominador)
        return Fraction(numerator=self.numerador * other, denominator=self.denominador)

    def __rmul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerador * other.numerador,
                            denominator=self.denominador * other.denominador)
        return Fraction(numerator=self.numerador * other, denominator=self.denominador)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerator=self.numerador * other.denominador,
                            denominator=self.denominador * other.numerador)
        return Fraction(numerator=self.numerador, denominator=self.denominador * other)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__numerador} / {self.__denominador}"

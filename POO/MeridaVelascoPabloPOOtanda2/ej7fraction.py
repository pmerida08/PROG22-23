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

    def __init__(self, numerador: int, denominador: int):
        if denominador == 0:
            raise ValueError('El denominador no puede ser 0.')

        mcd = math.gcd(numerador, denominador)

        self.__numerador = numerador // mcd
        self.__denominador = denominador // mcd

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
            return Fraction(numerador=self.numerador // mcm + other.numerador // mcm, denominador=mcm)
        return Fraction(numerador=self.numerador // mcm + other // mcm, denominador=mcm)

    def __sub__(self, other):
        mcm = (self.numerador * self.denominador) // math.gcd(self.numerador, self.denominador)
        if isinstance(other, Fraction):
            return Fraction(numerador=self.numerador // mcm - other.numerador // mcm, denominador= mcm)
        return Fraction(numerador=self.numerador // mcm - other // mcm, denominador= mcm)

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerador=self.numerador * other.numerador, denominador=self.denominador * other.denominador)
        return Fraction(numerador=self.numerador * other, denominador=self.denominador)

    def __rmul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerador=self.numerador * other.numerador, denominador=self.denominador * other.denominador)
        return Fraction(numerador=self.numerador * other, denominador=self.denominador)

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return Fraction(numerador=self.numerador * other.denominador, denominador=self.denominador * other.numerador)
        return Fraction(numerador=self.numerador, denominador=self.denominador * other)

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.__numerador} / {self.__denominador}"

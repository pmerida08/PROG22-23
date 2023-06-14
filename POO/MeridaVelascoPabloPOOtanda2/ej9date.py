"""
9. Nos hemos enterado de que la clase datetime.date ha sido comprometida y tenemos que crear una clase nueva para
almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los
objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de octubre de 2020
f2 = Date(f1) # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Crea métodos para:

    - Sumar y restar días a la fecha.
    - Restar fechas. Devuelve el número de días comprendidos entre ambas.
    - Comparar la fecha almacenada con otra.
    - Saber si el año de la fecha almacenada es bisiesto.
    - Obtener el día de la semana de una fecha concreta.
    - El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".
"""
from typeguard import typechecked


@typechecked
class Date:
    def __init__(self, day: int, month: int, year: int):
        leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if month == 2:
            if leap_year and day > 29:
                raise ValueError('El día de febrero en un año bisiesto no puede ser más de 29 días.')
            elif not leap_year and day > 28:
                raise ValueError('Febrero en un año no bisiesto no puede tener más de 28 días.')
        elif month in (4, 6, 9, 11) and day > 30:
            raise ValueError('Este mes no puede tener más de 30 días.')
        elif day > 31:
            raise ValueError('Los meses no tienen más de 31 días.')
        self.__day = day
        self.__month = month
        self.__year = year

    @classmethod
    def from_date(cls, other: 'Date'):
        return cls(other.__day, other.__month, other.__year)

    def copy(self):
        return self.__class__(self.__day, self.__month, self.__year)

    def operate_days(self, days: int):
        self.__day += days
        while True:
            leap_year = self.__year % 4 == 0 and (self.__year % 100 != 0 or self.__year % 400 == 0)
            if self.__month == 2:
                if leap_year and self.__day > 29:
                    self.__month += 1
                    self.__day -= 29
                    continue
                elif not leap_year and self.__day > 28:
                    self.__month += 1
                    self.__day -= 28
                    continue
            elif self.__month in (4, 6, 9, 11) and self.__day > 30:
                self.__month += 1
                self.__day -= 30
                continue
            elif self.__day > 31:
                self.__month += 1
                self.__day -= 31
                continue
            elif self.__month > 12:
                self.__year += 1
                continue
            break

    def compare_dates(self, other: 'Date'):
        if self.__year > other.__year:
            return f'La fecha "{repr(self)}" es mayor a "{repr(other)}"'
        if self.__year == other.__year:
            if self.__month > other.__month:
                return f'La fecha "{repr(self)}" es mayor a "{repr(other)}"'
            if self.__month == other.__month:
                if self.__day > other.__day:
                    return f'La fecha "{repr(self)}" es mayor a "{repr(other)}"'
                if self.__day == other.__day:
                    return f'La fecha "{repr(self)}" y "{repr(other)}" son iguales.'
                return f'La fecha {repr(self)} es menor a {repr(other)}'
            return f'La fecha {repr(self)} es menor a {repr(other)}'
        return f'La fecha {repr(self)} es menor a {repr(other)}'

    def days_between(self, other: 'Date'):  # TODO
        pass

    def leap_year(self):
        return self.__year % 4 == 0 and (self.__year % 100 != 0 or self.__year % 400 == 0)

    def day_of(self):
        first_date = Date(1, 1, 1)  # Ese día fue lunes
        total_days = 0
        while first_date != self:
            total_days += 1
            first_date += 1
        return total_days % 7

    def __repr__(self):
        return f"{self.__day:02d}/{self.__month:02d}/{self.__year:04d}"

    def __str__(self):
        months = (
            'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre',
            'noviembre',
            'diciembre')
        for month in range(12):
            if (month + 1) == self.__month:
                return f"{self.__day} de {months[month]} de {self.__year}"

"""
6. Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y
se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

    Sumar y restar objetos de la clase (el resultado es otro objeto).
    Sumar y restar segundos, minutos u horas (se cambia el objeto actual).
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
"""
from typeguard import typechecked


class Duration:

    @typechecked
    def __init__(self, hour: int = 0, minutes: int = 0, seconds: int = 0):

        while True:
            if seconds < 0:
                seconds = 60 - (-seconds)
                minutes -= 1
            elif minutes < 0:
                minutes = 60 - (-minutes)
                hour -= 1

            if seconds > 59:
                minutes += 1
                seconds -= 60
            elif minutes > 59:
                hour += 1
                minutes -= 60
            else:
                break
        self.__hour = hour
        self.__minutes = minutes
        self.__seconds = seconds

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):
        self.__hour = value

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value):
        self.__minutes = value

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value):
        self.__seconds = value

    @classmethod
    def from_duration(cls, other: 'Duration'):
        new_duration = cls()
        new_duration.__hour = other.__hour
        new_duration.__minutes = other.__minutes
        new_duration.__seconds = other.__seconds
        return new_duration

    def in_secs(self):
        return self.hour * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other):
        if isinstance(other, Duration):
            summ = Duration(self.hour + other.hour, self.minutes + other.minutes, self.seconds + other.seconds)
            return summ
        return Duration(seconds=self.in_secs() + other)

    def __sub__(self, other):
        if isinstance(other, Duration):
            sub = Duration(self.hour - other.hour, self.minutes - other.minutes, self.seconds - other.seconds)
            return sub
        return Duration(seconds=self.in_secs() + other)

    def __str__(self):
        return f"{self.__hour} horas, {self.__minutes} minutos, {self.__seconds} segundos"

    def __repr__(self):
        return f"{self.__hour} horas, {self.__minutes} minutos, {self.__seconds} segundos"

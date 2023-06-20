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


@typechecked
class Duration:

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):
            other = hours
            self.__hours, self.__minutes, self.__seconds = other.hours, other.minutes, other.seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
            self.__normalize()
        else:
            raise TypeError("Un objeto Duration se construye con tres enteros o con otro objeto Duration")

    def __total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __normalize(self):
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value: int):
        new_duration = Duration(value, self.minutes, self.seconds)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value: int):
        new_duration = Duration(self.hours, value, self.seconds)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value: int):
        new_duration = Duration(self.hours, self.minutes, value)
        self.__hours, self.__minutes, self.__seconds = new_duration.hours, new_duration.minutes, new_duration.seconds

    def in_secs(self):
        return self.hour * 3600 + self.minutes * 60 + self.seconds

    def __add__(self, other: 'Duration'):
        return Duration(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def __sub__(self, other: 'Duration'):
        return Duration(self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)

    def __eq__(self, other: 'Duration'):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __ne__(self, other: 'Duration'):
        return not self == other

    def __lt__(self, other: 'Duration'):
        return self.__total_seconds() < other.__total_seconds()

    def __le__(self, other: 'Duration'):
        return self.__total_seconds() <= other.__total_seconds()

    def __gt__(self, other: 'Duration'):
        return not self <= other

    def __ge__(self, other: 'Duration'):
        return not self < other

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.hours}, {self.minutes}, {self.seconds})"

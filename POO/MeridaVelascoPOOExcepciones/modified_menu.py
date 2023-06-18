"""
8. Muestra un menú con las siguientes opciones:

    - Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
    correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.

    - Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
    Si el número es negativo restará los días. Esta opción solo podrá realizarse si hay una fecha introducida
    (se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error.

    - Añadir meses a la fecha. El mismo procedimiento que la opción anterior.

    - Añadir años a la fecha. El mismo procedimiento que la opción 2.

    - Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da
    error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o
    posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.

    - Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").

    - Terminar.

Consideraciones a tener en cuenta:

    El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger
    alguna opción.
    Las fechas las manejaremos con la clase datetime.date.
"""
import datetime
from typeguard import typechecked
import sys


@typechecked
class DateFormatError(ValueError):

    def __init__(self, date_):
        super().__init__(f'El formato de la fecha {date_} es incorrecto')
        self.__date = date_


@typechecked
class Date:
    def __init__(self, day, month, year):
        self.date = datetime.datetime(year, month, day)

    def __str__(self):
        return self.date.strftime('%d/%m/%Y')

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.date.strftime('%d/%m/%Y')}"

    def add_days(self, days):
        self.date += datetime.timedelta(days=days)

    def add_months(self, months):
        new_month = (self.date.month + months) % 12
        new_year = self.date.year + ((self.date.month + months) // 12)
        try:
            self.date = self.date.replace(month=new_month, year=new_year)
        except ValueError:
            self.date = (datetime.date(self.date.year, self.date.month, 28) + datetime.timedelta(days=4)).replace(
                day=1) - datetime.timedelta(days=1)

    def add_years(self, years):
        try:
            self.date = self.date.replace(year=self.date.year + years)
        except ValueError:
            self.date = (datetime.date(self.date.year + years, self.date.month, 28) + datetime.timedelta(
                days=4)).replace(day=1) - datetime.timedelta(days=1)

    def compare(self, other):
        if isinstance(other, Date):
            if self.date > other.date:
                return 'La fecha almacenada es posterior a la fecha introducida'
            elif self.date == other.date:
                return 'La fecha almacenada es igual a la fecha introducida'
            return 'La fecha almacenada es anterior a la fecha introducida'
        return 'Error: el argumento no es una instancia de la clase Date'

    @staticmethod
    def check_date(date_):
        try:
            datetime.datetime.strptime(date_, '%d/%m/%Y')
            return True
        except ValueError:
            raise DateFormatError(date_)

    def long_format(self):
        days_week = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre',
                'noviembre', 'diciembre']
        day_week = days_week[self.date.weekday()]
        day = self.date.day
        month = months[self.date.month - 1]
        year = self.date.year
        self.check_date(self)
        return day_week + ', ' + str(day) + ' de ' + month + ' de ' + str(year)


@typechecked
class Menu:
    def __init__(self, title: str, *options: str):
        self.__title = title
        self.__options = list(options)

    def add(self, option):
        self.__options.append(option)

    def show(self):
        print(f'{self.__title}')
        for i, option in enumerate(self.__options):
            print(f'{i + 1}. {option}')

    def choose(self, option):
        if option == int:
            raise TypeError('El numero de la eleccion debe ser entero. Inténtalo otra vez.')
        return self.__options[option - 1]

    @staticmethod
    def check_date(fecha):
        try:
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
        except ValueError:
            raise DateFormatError(fecha)

    @staticmethod
    def exit():
        print("Saliendo del programa...")
        sys.exit()


if __name__ == '__main__':
    menu = Menu('Menú Fechas', 'Introducir una fecha (DD/MM/AAAA)', 'Añadir días', 'Añadir meses', 'Añadir años')
    menu.add('Compara la fecha con otra')
    menu.add('Mostrar la fecha con formato largo')
    menu.add('Terminar')
    menu.show()

    date = Date(5, 2, 2003)

    while True:
        opt = menu.choose(option=int(input('\nIntroduce la opción que desea escoger: ')))
        match opt:
            case 1:
                days_to_add = int(input('Introduce la cantidad de días que quieres añadir a la fecha: '))
                date.add_days(days_to_add)
                print(f'\nHas añadido {days_to_add} días más a la fecha')
            case 2:
                date.add_months(5)
            case 3:
                date.add_years(7)
            case 4:
                date.compare(Date(3, 5, 2004))
            case 5:
                date.long_format()
            case 6:
                menu.exit()

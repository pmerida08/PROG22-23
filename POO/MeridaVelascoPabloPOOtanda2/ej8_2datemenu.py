"""
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

"""
from typeguard import typechecked
from ej8_1menu import Menu
import datetime

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

    def long_format(self):
        days_week = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
        months = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre',
                  'noviembre', 'diciembre']
        day_week = days_week[self.date.weekday()]
        day = self.date.day
        month = months[self.date.month - 1]
        year = self.date.year
        return day_week + ', ' + str(day) + ' de ' + month + ' de ' + str(year)


if __name__ == '__main__':
    menu = Menu('Menú Fechas', 'Añadir días', 'Añadir meses', 'Añadir años')
    menu.add('Compara la fecha con otra')
    menu.add('Mostrar la fecha con formato largo')
    menu.add('Terminar')
    menu.show()

    date = Date(5, 2, 2003)

    while True:
        option = menu.choose(option=int(input('Introduce la opción que desea escoger: ')))
        match option:
            case 1:
                print(menu[option])
                date.add_days(4)
            case 2:
                print(menu[option])
                date.add_months(5)
            case 3:
                print(menu[option])
                date.add_years(7)
            case 4:
                print(menu[option])
                date.compare(Date(3, 5, 2004))
            case 5:
                print(menu[option])
                date.long_format()
            case 6:
                print(menu[option])
                menu.exit()

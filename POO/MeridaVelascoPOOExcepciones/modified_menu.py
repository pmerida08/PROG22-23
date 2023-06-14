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

    El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger alguna opción.
    Las fechas las manejaremos con la clase datetime.date.
"""
from typeguard import typechecked
import sys


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
            return self.__options[option - 1]
        raise TypeError('El numero de la eleccion debe ser entero. Inténtalo otra vez.')

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

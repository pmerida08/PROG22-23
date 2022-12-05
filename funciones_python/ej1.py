"""
    Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
    multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
    el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se
    volverá a mostrar, a menos que no sé de a la opción terminar.

    Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
    Las variables se inicializan a cero.

    Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se
    puedan ejecutar el resto de las opciones.

    Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción (por su
    número) y devuelve la opción escogida. Modifica el último programa para que use esta función.

    Autor: Pablo Mérida Velasco
    Fecha: 01/12/2022
"""

import sys

print('Menu: ')
print('1. Sumar' + '\n'
      '2. Restar' + '\n'
      '3. Multiplicar' + '\n'
      '4. Dividir' + '\n'
      '5. Salir')
print('---------------------------------------------------------------------------------------------------------------')

# El método "match" funciona a partir de Python 3.10
while True:
    opcion = int(input('Introduce la acción que desee hacer: '))
    match opcion:
        case 1:
            print('Has elegido la opción 1')
        case 2:
            print('Has elegido la opción 2')
        case 3:
            print('Has elegido la opción 3')
        case 4:
            print('Has elegido la opción 4')
        case 5:
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(1)
        case _:
            print('La opcion no es correcta')
            break

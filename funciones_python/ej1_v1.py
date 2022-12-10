"""
    Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
    multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra
    el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se
    volverá a mostrar, a menos que no sé de a la opción terminar.

    Autor: Pablo Mérida Velasco
    Fecha: 01/12/2022
"""

import sys


def exit_program():
    print('Has salido del programa con éxito.', file=sys.stderr)
    sys.exit(1)


def summary(a, b):
    sum_nums = a + b
    return print(f'La suma de los números dados es de: {sum_nums}')


def substract(a, b):
    subst_nums = a - b
    return print(f'La resta de los números dados es de: {subst_nums}')


def multi(a, b):
    multi_nums = a * b
    return print(f'La multiplicación de los números dados es de: {multi_nums}')


def divide(a, b):
    div_nums = 0.0
    if b != 0:
        div_nums = a / b
    else:
        print('No se puede dividir un número entre 0.')
    return print(f'La división de los números dados es de: {div_nums}')


num1 = int(input('Introduce un número para el valor de A: '))
num2 = int(input('Introduce un número para el valor de B: '))


print('\nMenu: ')
print('1. Sumar' + '\n'
      '2. Restar' + '\n'
      '3. Multiplicar' + '\n'
      '4. Dividir' + '\n'
      '5. Salir')
print('---------------------------------------------------------------------------------------------------------------')

# El método "match" funciona a partir de Python 3.10
while True:
    opcion = int(input('\nIntroduce la acción que desee hacer: '))
    match opcion:
        case 1:
            summary(num1, num2)
        case 2:
            substract(num1, num2)
        case 3:
            multi(num1, num2)
        case 4:
            divide(num1, num2)
        case 5:
            exit_program()
        case _:
            print('La opcion no es correcta')
            break

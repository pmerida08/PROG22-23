"""
    Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera).
    Las variables se inicializan a cero.

    Autor: Pablo Mérida Velasco
    Fecha: 08/12/2022
"""

import sys


def input_values():
    num = int(input('Introduce el valor de un número para un valor: '))
    return num


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


num_a = 0
num_b = 0


print('\nMenu: ')
print('0. Introducir número' + '\n'
      '1. Sumar' + '\n'
      '2. Restar' + '\n'
      '3. Multiplicar' + '\n'
      '4. Dividir' + '\n'
      '5. Salir')
print('---------------------------------------------------------------------------------------------------------------')


def input_variables():
    global num_a, num_b
    num_a = int(input('Introduce el valor de un número para un valor: '))
    num_b = int(input('Introduce el valor de un número para un valor: '))


# El método "match" funciona a partir de Python 3.10
while True:
    opcion = int(input('\nIntroduce la acción que desee hacer: '))
    match opcion:
        case 0:
            input_variables()
        case 1:
            summary(num_a, num_b)
        case 2:
            substract(num_a, num_b)
        case 3:
            multi(num_a, num_b)
        case 4:
            divide(num_a, num_b)
        case 5:
            exit_program()
        case _:
            print('La opcion no es correcta')
            break

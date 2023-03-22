"""
    Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se
    puedan ejecutar el resto de las opciones.

    Autor: Pablo Mérida Velasco
    Fecha: 08/12/2022
"""

import sys


def input_values():
    num = int(input('Introduce el valor de un número para un valor: '))
    return num


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


def exit_program():
    print('Has salido del programa con éxito.', file=sys.stderr)
    sys.exit(1)


num1 = 0
num2 = 0
condition_to_input = False


print('\nMenu: ')
print('0. Introducir número' + '\n'
      '1. Sumar' + '\n'
      '2. Restar' + '\n'
      '3. Multiplicar' + '\n'
      '4. Dividir' + '\n'
      '5. Salir')
print('---------------------------------------------------------------------------------------------------------------')

# El método "match" funciona a partir de Python 3.10
while True:
    opcion = int(input('\nIntroduce la acción que desee hacer: '))
    match opcion:
        case 0:
            num1 = input_values()
            num2 = input_values()
            condition_to_input = True
        case 1:
            if condition_to_input:
                summary(num1, num2)
            else:
                print('No puedes hacer una suma sin introducir antes los valores.')
                continue
        case 2:
            if condition_to_input:
                substract(num1, num2)
            else:
                print('No puedes hacer una resta sin introducir antes los valores.')
                continue
        case 3:
            if condition_to_input:
                multi(num1, num2)
            else:
                print('No puedes hacer una multiplicación sin introducir antes los valores.')
                continue
        case 4:
            if condition_to_input:
                divide(num1, num2)
            else:
                print('No puedes hacer una división sin introducir antes los valores.')
                continue
        case 5:
            exit_program()
        case _:
            print('La opcion no es correcta. Inténtalo de nuevo')
            continue

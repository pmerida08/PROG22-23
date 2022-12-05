"""
Realiza un programa que pida cinco números enteros y diga cuál es el mayor.

Autor: Pablo Mérida Velasco
Fecha: 18/10/2022
"""

# ***
import sys

print('Este programa pide cinco números enteros y dice cuál es el mayor.')

num1 = input('Introduce el valor de número 1: ')
num2 = input('Introduce el valor de número 2: ')
maximo = 0

if num1.isdigit() and num2.isdigit():
    if num1 > num2:
        maximo = num1
        print(f'El número mayor es el numero: {maximo}')
    else:
        maximo = num2
        print(f'El número mayor es el numero: {maximo}')

    num3 = input('Introduce el valor de número 3: ')
    if maximo > num3:
        print(f'El número mayor es el numero: {maximo}')
    else:
        maximo = num3
        print(f'El número mayor es el numero: {maximo}')

    num4 = input('Introduce el valor de número 3: ')
    if maximo > num4:
        print(f'El número mayor es el numero: {maximo}')
    else:
        maximo = num4
        print(f'El número mayor es el numero: {maximo}')

    num5 = input('Introduce el valor de número 3: ')
    if maximo > num5:
        print(f'El número mayor es el numero: {maximo}')
    else:
        maximo = num5
        print(f'El número mayor es el numero: {maximo}')
else:
    print('Los números dados no son dígitos.', file=sys.stderr)
    sys.exit(1)

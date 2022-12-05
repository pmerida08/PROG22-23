"""
Realiza un programa que pida tres números enteros y diga cuál es el mayor.

Autor: Pablo Mérida Velasco
Fecha: 18/10/2022
"""
import sys

# ***
print('Este programa pide tres números enteros y dice cuál es el mayor.')

try:
    num1 = int(input('Introduce el valor de número 1: '))
    num2 = int(input('Introduce el valor de número 2: '))
    num3 = int(input('Introduce el valor de número 3: '))
except ValueError:
    print("Ha introducido un valor que no es entero", file=sys.stderr)
    sys.exit(1)

if num1 > num2 > num3 or num1 > num3 > num1:
    print(f'El número {num1} es el mayor.')
elif num2 > num1 > num3 or num2 > num3 > num1:
    print(f'El número {num2} es el mayor.')
else:
    print(f'El número {num3} es el mayor.')

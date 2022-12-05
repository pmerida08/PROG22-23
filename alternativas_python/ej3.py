"""
Escribe un programa que lea un número e indique si es par o impar.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

num = int(input('Introduce un número: '))

if num % 2 == 0:
    print(f'El número {num} es par.')
else:
    print(f'El número {num} es impar.')

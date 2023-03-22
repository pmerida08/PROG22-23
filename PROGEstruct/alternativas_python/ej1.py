"""
Programa que pida dos números e indique si el primero es mayor que el segundo o no.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

n1 = int(input('Dime un número: '))
n2 = int(input('Dime otro número: '))

if n1 > n2:
    print(f'El número {n1} es mayor que el número {n2}')
else:
    print(f'El número {n1} es menor que el número {n2}')

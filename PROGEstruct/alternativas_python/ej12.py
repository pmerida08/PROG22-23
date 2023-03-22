"""
Escribir un programa que lea un año indicar si es bisiesto.

Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea
divisible por 400.

Autor: Pablo Mérida Velasco
Fecha: 16/10/2022
"""

anio = int(input('Introduce un año: '))

if anio % 4 == 0 and (anio % 400 == 0 or anio % 100 != 0):
    print(f'El año {anio} es bisiesto.')
else:
    print(f'El año {anio} no es bisiesto.')

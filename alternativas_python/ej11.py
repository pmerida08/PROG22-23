"""
Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar que tipo de triángulo es, teniendo en cuenta los siguientes:

    Si se cumple Pitágoras entonces es triángulo rectángulo
    Si solo dos lados del triángulo son iguales entonces es isósceles.
    Si los 3 lados son iguales entonces es equilátero.
    Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Autor: Pablo Mérida Velasco
Fecha: 15/10/2022
"""

a = int(input('Introduce un valor para la variable A del triángulo: '))
b = int(input('Introduce un valor para la variable B del triángulo: '))
c = int(input('Introduce un valor para la variable C del triángulo: '))

if c == a ** 2 + b ** 2 or b == a ** 2 + c ** 2 or a == b ** 2 + c ** 2:
    print('Es un triángulo rectángulo.')
elif (a == b and c) or (b == a and c) or (c == b and a):
    print('Es un triángulo isósceles.')
elif a == b == c:
    print('El triángulo es equilátero.')
else:
    print('El triángulo es escaleno.')

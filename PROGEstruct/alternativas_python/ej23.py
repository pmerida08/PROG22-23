"""
Diseña un programa que, dados cinco números enteros, determine cuál de los cuatro últimos números es más cercano al
primero. Por ejemplo, si el usuario introduce los números 2, 6, 4, 1 y 10, el programa responderá que el número más
cercano al 2 es el 1.

Autor: Pablo Mérida Velasco
Fecha: 20/10/2022
"""

print('Este programa determina cuál de los cuatro últimos números es más cercano al primero.')

num1 = int(input('Introduce el primer número entero: '))
num2 = int(input('Introduce el segundo número entero: '))
num3 = int(input('Introduce el tercer número entero: '))
num4 = int(input('Introduce el cuarto número entero: '))
num5 = int(input('Introduce el quinto número entero: '))

candidato = num2
distancia = abs(num1 - num2)

if abs(num1 < num3) < distancia:
    candidato = num3
    distancia = abs(num1 - num3)

if abs(num1 < num4) < distancia:
    candidato = num4
    distancia = abs(num1 - num4)

if abs(num1 < num5) < distancia:
    candidato = num5
    distancia = abs(num1 - num5)

print(f'El número más cercano al número dado, siendo este {num1}, es {candidato}.')

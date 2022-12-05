"""
Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""

print('Este programa pide un rango de números y te dice los números pares que hay entre ellos.')

num1 = int(input('Introduce el primer número para el rango: '))
num2 = int(input('Introduce el segundo número para el rango: '))
counter = 0

if num2 > num1:
    counter = 1
else:
    counter = -1

print(f'Los números pares entre el {num1} y el {num2} son: ')
for i in range(num1, num2, counter):
    if i % 2 == 0:
        print(f'{i}', end=" ")

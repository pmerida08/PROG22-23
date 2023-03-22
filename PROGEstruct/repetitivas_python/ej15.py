"""
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual
adelante que atrás.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""

print('Este programa te dice si es una palabra palíndroma o no.')

string1 = input('Introduce una cadena por teclado: ')
reversed_string = string1[::-1]

if string1 == reversed_string:
    print(f'{string1} es una palabra palíndroma.')
else:
    print(f'{string1} no es una palabra palíndroma.')

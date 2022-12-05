"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

print('Identifica si es una letra mayúscula o minúscula.')

cadena = input('Introduce una cadena: ')

if len(cadena) == 1 and cadena.isalpha():
    if cadena.isupper():
        print('Es una letra mayúcula.')
    else:
        print('No es una letra mayúscula.')
else:
    print('No es una letra.')

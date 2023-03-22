"""
Pide una cadena y dos caracteres por teclado (verifica que sea un carácter), sustituye la aparición del primer carácter
en la cadena por el segundo carácter.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""
import sys

print('Este programa sustituye el carácter que coincide con una cadena introducida, por otro carácter.')

string = input('Introduce una cadena por teclado: ')
character1 = input('Introduce un carácter por teclado: ')
character2 = input('Introduce otro carácter por teclado: ')

if len(character1) > 1 or len(character2) > 1:
    print(f'{character1} no es un carácter.', file=sys.stderr)
    sys.exit(1)

new_string = string.replace(character1, character2)
print(new_string)

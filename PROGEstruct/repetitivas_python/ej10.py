"""
Pide una cadena y un carácter por teclado y muestra cuantas veces aparece el carácter en la cadena.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""
import sys

# Este programa hace que se cuenten las veces que aparece un carácter en una cadena.

string1 = input('Introduce una cadena por teclado: ')
character = input('Introduce un carácter por teclado: ')
n = [n for n in (list(string1))]
num_character_founded = 0

if len(character) > 1:
    print(f'{character} no es un carácter.', file=sys.stderr)
    sys.exit(1)

for i in n:
    if character == i:
        num_character_founded += 1

print(f'Hay {num_character_founded} carácteres en esta cadena.')

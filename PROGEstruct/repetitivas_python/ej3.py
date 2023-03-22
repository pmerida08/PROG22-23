"""
Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina
cuando se introduce un espacio.

Autor: Pablo Mérida Velasco
Fecha: 26/10/2022
"""
import sys

VOWELS = 'aeiouáéíóúAEIOUÁÉÍÓÚ'

while True:
    character = input('Introduce una letra: ')

    if len(character) != 1 or character.isdigit():
        print(f'{character} no es un carácter válido.', file=sys.stderr)
        sys.exit(1)

    if character == ' ':
        break

    if character in VOWELS:
        print('El carácter introducido es una VOCAL.')
    else:
        print('El carácter introducido NO ES VOCAL.')



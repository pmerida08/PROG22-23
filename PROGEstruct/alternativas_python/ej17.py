"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre
por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.

    Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
    Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número
    incorrecto.”.

Autor: Pablo Mérida Velasco
Fecha: 20/10/2022
"""

import sys

print('Este programa dice la cara opuesta del dado que se ha lanzado')
print('------------------------------------------------------------- ')

result = int(input('Introduce el valor de la cara del dado que ha salido: '))

if 0 < result <= 6:
    if result == 1:
        print(f'La cara opuesta del dado con el valor: {result} es el 6')
    elif result == 2:
        print(f'La cara opuesta del dado con el valor: {result} es el 5')
    elif result == 3:
        print(f'La cara opuesta del dado con el valor: {result} es el 4')
    elif result == 4:
        print(f'La cara opuesta del dado con el valor: {result} es el 3')
    elif result == 5:
        print(f'La cara opuesta del dado con el valor: {result} es el 2')
    else:
        print(f'La cara opuesta del dado con el valor: {result} es el 1')
else:
    print('ERROR: número incorrecto.', file=sys.stderr)
    sys.exit(1)

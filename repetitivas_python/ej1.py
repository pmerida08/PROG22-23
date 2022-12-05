"""
Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio
del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar
es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10
intentos para acertarlo). El programa termina cuando se acierta el número (además te dice
en cuantos intentos lo has acertado), si se llega al límite de intentos te muestra el número que había generado.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""
import random
import sys

MAXIMUM_RANGE = 101
MINIMUM_RANGE = 1

print('Este programa nos da un número entre el 1 y el 100 y el usuario debe adivinarlo.')
print('--------------------------------------------------------------------------------')

num_aleatorio = random.randrange(MINIMUM_RANGE, MAXIMUM_RANGE)
num_introducido = int(input('Introduce un número del 1 al 100: '))
intentos = 10

if 0 < num_introducido <= 100:
    while True:
        if num_introducido == num_aleatorio:
            print(f'Has acertado el número en {10 - intentos} intentos.')
            break
        else:
            intentos -= MINIMUM_RANGE
            if 0 < num_introducido <= 100:
                print(f'Te quedan {intentos} intentos.')
                if num_introducido < num_aleatorio:
                    print('El número a adivinar es mayor.')
                else:
                    print('El número a adivinar es menor.')
                num_introducido = int(input('Has fallado el número. Prueba otra vez: '))
            else:
                print(f'El número {num_introducido} es inválido.', file=sys.stderr)
                sys.exit(1)
        if intentos <= MINIMUM_RANGE:
            print(f'Te has quedado sin intentos. El número era el {num_aleatorio}')
            break
else:
    print(f'El número {num_introducido} es inválido.', file=sys.stderr)
    sys.exit(1)

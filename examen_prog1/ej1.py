"""
1. Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras. El
programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje “Lo
siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto
satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.

Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera
anormal con un mensaje de error.

Nombre: Pablo Mérida Velasco
Curso: 1DAW A
Fecha: 10/11/2022

"""
import random
import sys

print('Este programa consiste en adivinar una combinación de una caja fuerte con una contraseña de 4 dígitos')

# Declaramos variables
ATTEMPTS = 4
combination_to_open = random.randint(1000, 10000)

# Desarrollamos el algoritmo
while ATTEMPTS > 0:
    guess_combination = input('Introduce un número de cuatro dígitos para intentar adivinar la contraseña de la caja'
                              ' fuerte: ')

    if guess_combination == '' or len(str(guess_combination)) != 4 or not str(guess_combination).isnumeric():
        print('El valor introducido es inválido.', file=sys.stderr)
        sys.exit(1)

    if guess_combination == combination_to_open:
        print('La caja fuerte se ha abierto satisfactoriamente')
        break
    else:
        ATTEMPTS -= 1
        if ATTEMPTS == 0:
            print('Has fallado. Te has quedado sin intentos.')
            print(f'La combinacion era: {combination_to_open}')
        else:
            print('Lo siento, esa no es la combinación')
            print(f'Te quedan {ATTEMPTS} intentos.')

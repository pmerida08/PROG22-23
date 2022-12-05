"""
4. Según cierta cultura oriental, los números de la suerte son el 3, el 7, el 8 y el 9. Los números de la
mala suerte son el resto: el 0, el 1, el 2, el 4, el 5 y el 6. Un número es afortunado si contiene más
números de la suerte que de la mala suerte. Realiza un programa que diga si un número introducido
por el usuario es afortunado o no.

Ejemplo 1: Introduzca un número: 772
El 772 es un número afortunado.

Ejemplo 2: Introduzca un número: 7720
El 7720 no es un número afortunado.

Ejemplo 3: Introduzca un número: 43081
El 43081 no es un número afortunado.

Ejemplo 4: Introduzca un número: 888
El 888 es un número afortunado.

Ejemplo 5: Introduzca un número: 1234
El 1234 no es un número afortunado.

Ejemplo 6: Introduzca un número: 6789
El 6789 es un número afortunado.

Nombre: Pablo Mérida Velasco
Curso: 1DAW A
Fecha: 10/11/2022

"""
import sys

print('Este programa calcula si el número introducido es un número afortunado o no, según una cultura oriental.')

# Declaramos las variables
lucky_num = '3789'
lucky_in = 0
unlucky_in = 0
num_to_check = input('Introduce un número para ver si es afortunado o no: ')

# Desarrollamos el algoritmo
if not num_to_check.isnumeric():
    print('El valor introducido no es válido.', file=sys.stderr)
    sys.exit(1)

for i in num_to_check:
    if i in lucky_num:
        lucky_in += 1
    else:
        unlucky_in += 1

if lucky_in > unlucky_in:
    print(f'{num_to_check} es un número afortunado.')
else:
    print(f'El {num_to_check} no es un número afortunado.')

"""
Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos
otro número nos da un error.

Autor: Pablo Mérida Velasco
Fecha: 20/10/2022
"""

import sys

print('Este programa dice el día correspondiente al número del día de la semana.')

numero_dia = int(input('Introduce el número del día de la semana que desea saber: '))

if 0 < numero_dia <= 7:
    if numero_dia == 1:
        print('El día de la semana introducido es LUNES.')
    elif numero_dia == 2:
        print('El día de la semana introducido es MARTES.')
    elif numero_dia == 3:
        print('El día de la semana introducido es MIÉRCOLES.')
    elif numero_dia == 4:
        print('El día de la semana introducido es JUEVES.')
    elif numero_dia == 5:
        print('El día de la semana introducido es VIERNES.')
    elif numero_dia == 6:
        print('El día de la semana introducido es SÁBADO.')
    else:
        print('El día de la semana introducido es DOMINGO.')
else:
    print('No es un número de día de la semana válido.', file=sys.stderr)
    sys.exit(1)

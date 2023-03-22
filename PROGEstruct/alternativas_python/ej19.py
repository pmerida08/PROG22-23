"""
Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes
correspondiente.

Autor: Pablo Mérida Velasco
Fecha: 18/10/2022
"""
import sys

numero_mes = int(input('Introduce el número del mes que desee: '))

if 0 < numero_mes <= 12:
    if numero_mes == 2:
        print(f'El mes correspondiente al día {numero_mes} tiene 28 días en un año normal, si es año bisiesto 29 días.')
    elif numero_mes == 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f'El mes correspondiente al día {numero_mes} tiene 31 días.')
    else:
        print(f'El mes correspondiente al día {numero_mes} tiene 30 días.')
else:
    print('El número introducido no corresponde con ningún número del mes.', file=sys.stderr)
    sys.exit(1)

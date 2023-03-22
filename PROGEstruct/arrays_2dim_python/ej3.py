"""
Modifica el programa anterior de tal forma que las sumas parciales y la suma total aparezcan en la pantalla con un
pequeño retardo, dando la impresión de que el ordenador se queda “pensando” antes de mostrar los números.

Autor: Pablo Mérida Velasco
Fecha: 17/11/2022
"""

import time
import random

ROWS = 4
COLUMNS = 5

array = [[0] * COLUMNS for _ in range(ROWS)]  # Inicializamos array a 0

# Petición de datos

for i in range(ROWS):
    for j in range(COLUMNS):
        random_num = random.randint(100, 1000)
        array[i][j] = random_num

# Imprimir filas y sumatorio de cada fila

for i in range(ROWS):
    sum_rows = 0
    for j in range(COLUMNS):
        sum_rows += array[i][j]
        print(f'{array[i][j]:5d} ', end='')
    print(f'| {sum_rows:6d}')

# Imprimir sumatorio total y sumatorio de cada columna

print('-' * (4*(COLUMNS+1) + 1))  # separador
sum_total = 0

for j in range(COLUMNS):
    sum_columns = 0
    for i in range(ROWS):
        sum_columns += array[i][j]
    time.sleep(0.5)
    print(f'{sum_columns:5d} ', end='')
    sum_total += sum_columns
time.sleep(0.5)
print(f'| {sum_total:6d}')

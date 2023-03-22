"""
Realiza un programa que rellene un array de 6 filas por 10 columnas con números enteros positivos comprendidos
entre 0 y 1000 (ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como
del mínimo.

Autor: Pablo Mérida Velasco
Fecha: 17/11/2022
"""
import random

ROWS = 6
COLUMNS = 10

array = [[0] * COLUMNS for _ in range(ROWS)]

for i in range(ROWS):
    for j in range(COLUMNS):
        random_num = random.randrange(1001)
        array[i][j] = random_num

maximum = 0
minimum = 0
posicion_maximo_x = 0
posicion_maximo_y = 0
posicion_minimo_x = 0
posicion_minimo_y = 0

for i in range(ROWS):
    for j in range(COLUMNS):
        print(f'{array[i][j]:5d} ', end='')
        if array[i][j] > maximum:
            maximum = array[i][j]
            posicion_maximo_x = i
            posicion_maximo_y = j
        if array[i][j] < minimum:
            minimum = array[i][j]
            posicion_minimo_x = i
            posicion_minimo_y = j
    print('')
print(f'Máximo: ({posicion_maximo_x},{posicion_maximo_y}) |  Mínimo: ({posicion_minimo_x},{posicion_minimo_y})')

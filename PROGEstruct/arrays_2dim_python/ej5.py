"""
Modifica el programa anterior de tal forma que no se repita ningún número en el array.

Autor: Pablo Mérida Velasco
Fecha: 17/11/2022
"""

import random

ROWS = 2
COLUMNS = 2
LOWEST_NUM = 0
BIGGEST_NUM = 10

array = [[None] * COLUMNS for _ in range(ROWS)]

for row in range(ROWS):
    for column in range(COLUMNS):
        # generamos un número que no esté en el array
        while True:
            is_number_in_array = False
            n = random.randint(LOWEST_NUM, BIGGEST_NUM)
            for i in range(row+1):
                if n in array[i]:
                    is_number_in_array = True
                    break
            if not is_number_in_array:
                break
        array[row][column] = n

maximum = 0
minimum = 0
posicion_maximo_x = 0
posicion_maximo_y = 0
posicion_minimo_x = 0
posicion_minimo_y = 0

for i in range(ROWS):
    for j in range(COLUMNS):
        print(f'{array[i][j]:5d} ', end='')
        if array[i][j] < minimum:
            minimum = array[i][j]
            posicion_minimo_x = i
            posicion_minimo_y = j
        if array[i][j] > maximum:
            maximum = array[i][j]
            posicion_maximo_x = i
            posicion_maximo_y = j
    print('')
print(f'Máximo: ({posicion_maximo_x},{posicion_maximo_y}) |  Mínimo: ({posicion_minimo_x},{posicion_minimo_y})')

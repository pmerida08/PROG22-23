"""
Ejercicio 1

Escribe un programa que pida 20 números enteros. Estos números se deben introducir en un array de 4 filas por 5
columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.

Autor: Pablo Mérida Velasco
Fecha: 14/11/2022
"""
ROWS = 2
COLUMNS = 3

array = [[0] * COLUMNS for _ in range(ROWS)]  # Inicializamos array a 0

# Petición de datos

for i in range(ROWS):
    for j in range(COLUMNS):
        array[i][j] = int(input(f'Dame el valor del array de la posición {i}, {j}: '))

# Imprimir filas y sumatorio de cada fila

for i in range(ROWS):
    sum_rows = 0
    for j in range(COLUMNS):
        sum_rows += array[i][j]
        print(f'{array[i][j]:3d} ', end='')
    print(f'| {sum_rows:4d}')

# Imprimir sumatorio total y sumatorio de cada columna

print('-' * (4*(COLUMNS+1) + 1))  # separador
sum_total = 0

for j in range(COLUMNS):
    sum_columns = 0
    for i in range(ROWS):
        sum_columns += array[i][j]
    print(f'{sum_columns:3d} ', end='')
    sum_total += sum_columns
print(f'| {sum_total:4d}')

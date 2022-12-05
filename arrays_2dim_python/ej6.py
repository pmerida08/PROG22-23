"""
Realiza un programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países. El
array que contiene los nombres de los países es el siguiente:

paises = [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar. Los nombres de los países se deben
mostrar utilizando el array de países (no se pueden escribir directamente).

Autor: Pablo Mérida Velasco
Fecha: 17/11/2022
"""
import random

ROWS = 4
COLUMNS = 10
countries = ('España', 'Rusia', 'Japón', 'Australia')
minimum = 140
maximum = 211
array = [[None] * COLUMNS for _ in range(ROWS)]
mean = 0

print(f'{"MIN | MAX | MED":>89}')
for row in range(ROWS):
    print(f'{countries[row]:<12}', end='')
    minimum = 140
    maximum = 211
    summary = 0
    for column in range(COLUMNS):
        random_num = random.randint(140, 211)
        array[row][column] = random_num
        print(f'{array[row][column]:<6d}', end='')
        if array[row][column] >= minimum:
            minimum = array[row][column]
        if array[row][column] <= maximum:
            maximum = array[row][column]
        summary += random_num
    mean = summary / COLUMNS
    print(f'| {minimum:3} ', end='')
    print(f'| {maximum:3} |', end='')
    print(f' {mean:3}', end='')
    print('')



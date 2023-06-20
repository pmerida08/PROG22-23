"""
3. Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero. Tanto el nombre del fichero
como la palabra se deben pasar como argumentos en la línea de comandos.

"""
import sys

try:
    text_file = sys.argv[1]
    word = sys.argv[2]

    count = 0
    with open(text_file, 'r', encoding='utf-8') as file:
        for line in file:
            count += line.count(word)

    print(f'La palabra {word} se repite {count} veces.')
except IndexError:
    print('La cantidad de parámetros que se le pasa al programa al ejecutarse es incorrecta.')

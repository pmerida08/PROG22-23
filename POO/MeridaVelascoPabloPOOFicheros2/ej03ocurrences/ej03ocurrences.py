"""
3. Realiza un programa que diga cuántas ocurrencias de una palabra hay en un fichero. Tanto el nombre del fichero
como la palabra se deben pasar como argumentos en la línea de comandos.

"""

word = input('Di la palabra que quieras ver cuantas ocurrencias hay en el archivo: ')

count = 0
with open('file.txt', 'r+t', encoding='utf-8') as file:
    for line in file:
        count += line.count(word)

print(f'La palabra {word} se repite {count} veces.')
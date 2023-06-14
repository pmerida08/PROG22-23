"""
1. Realiza un programa que sea capaz de ordenar alfabéticamente las palabras contenidas en un fichero de texto.
El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos. El nombre del
fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo palabras_sort.txt.
Suponemos que cada palabra ocupa una línea.
"""
WORDS = 5

listing_words = []
sorted_words = []

with open('ej1ordenar.txt', 'rt', encoding='utf-8') as file:
    for _ in range(WORDS):
        line = file.readline().rstrip()
        listing_words.append(line)

sorted_words = sorted(listing_words)

with open('ej1ordenar_sorted.txt', 'r+t', encoding='utf-8') as file:
    for word in sorted_words:
        file.write(word + '\n')

"""
4. Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior. El programa
irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si son correctas.
Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 21/03/2023
"""
import random

WORDS = {
    'coche': 'car',
    'plato': 'dish',
    'botella': 'bottle',
    'raton': 'mouse',
    'mando': 'controller',
    'camara': 'cam',
    'pastilla': 'pill',
    'altavoz': 'speaker',
    'pan': 'bread',
    'ordenador': 'computer',
    'casa': 'house',
    'cargador': 'charger',
    'cuchara': 'spoon',
    'basura': 'trash',
    'cama': 'bed',
    'lata': 'can',
    'programa': 'program',
    'pagina': 'page',
    'desarrollador': 'developer',
    'consola': 'console',
    'maestro': 'master'
}
attempts = 0
TOTAL_ATTEMPTS = 5

total_corrects = 0
total_incorrect = 0

while attempts < TOTAL_ATTEMPTS:
    to_translate = random.choice(list(WORDS))
    in_english = input(f'Introduce la traduccion de la palabra "{to_translate}": ')
    if WORDS[to_translate] ==  in_english:
        total_corrects += 1
        attempts += 1
        continue
    else:
        total_incorrect += 1
        attempts += 1
        continue
print(f'Has acertado {total_corrects} palabras y has fallado {total_incorrect}')




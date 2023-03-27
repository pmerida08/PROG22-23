"""
3. Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción).
Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará la
correspondiente traducción en inglés.

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

while True:
    to_translate = random.choice(list(WORDS))
    in_english = input(f'Introduce la traduccion de la palabra "{to_translate}": ')
    if WORDS[to_translate] ==  in_english:
        print(f'Has acertado, la traducción de "{to_translate}" es "{in_english}".')
        break
    else:
        print(f'No es {in_english}. Vuelve a intentarlo')
        continue

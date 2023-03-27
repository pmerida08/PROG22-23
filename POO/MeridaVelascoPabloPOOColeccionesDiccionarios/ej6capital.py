"""
6. Realiza un programa que sepa decir la capital de un país (en caso de conocer la respuesta) y que, además, sea capaz
de aprender nuevas capitales. En principio, el programa solo conoce las capitales de España, Portugal y Francia. Estos
datos deberán estar almacenados en un diccionario. Los datos sobre capitales que vaya aprendiendo el programa se deben
almacenar en el mismo diccionario. El usuario sale del programa escribiendo la palabra “salir”.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 26/03/2023
"""
import sys

country_and_capitals = {
    'Espana': 'Madrid',
    'Francia': 'Paris',
    'Portugal': 'Lisboa'
}

while True:
    country = input('Introduce un pais y te diré su capital ("salir", para salir del programa"): ')
    if country == 'salir':
        print('Has salido del programa.', file=sys.stderr)
        sys.exit(1)

    if country in country_and_capitals:
        print(f'La capital de {country} es {country_and_capitals[country]}')
    else:
        capital_new_city = input('Oh, no logro encontrar la ciudad, ¿me podrías decir cuál es su capital para añadirla a la lista?: ')
        country_and_capitals[country] = capital_new_city
        print('Ciudad y capital añadida.')

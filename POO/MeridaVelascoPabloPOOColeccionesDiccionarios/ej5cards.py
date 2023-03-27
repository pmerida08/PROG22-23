"""
5. Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según el juego
de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener parejas (figura, valor), por
ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta. El valor de
las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto de cartas no vale nada.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 26/03/2023
"""
from POO.MeridaVelascoPabloPOOtanda3.ej14deck.card import Card
import random

NUMBERS = "1 2 3 4 5 6 7 8 9 SOTA CABALLO REY".split()
SUITS = "OROS COPAS ESPADAS BASTOS".split()

VALUES = {
    'AS': 11,
    'TRES': 10,
    'SOTA': 2,
    'CABALLO': 3,
    'REY': 4
}

puntuation = 0
pairs = list()

for _ in range(5):
    chosen_number = random.choice(NUMBERS)
    for key in VALUES:
        if chosen_number == key:
            puntuation += VALUES[key]
    chosen_suits = random.choice(SUITS)
    card = Card(chosen_number, chosen_suits)
    pairs.append(card)
print(pairs)
print(f'La puntación es de: {puntuation}')

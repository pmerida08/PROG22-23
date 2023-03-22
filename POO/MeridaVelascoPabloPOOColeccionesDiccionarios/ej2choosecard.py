"""
2. Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase Carta). Emplea una
lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas. Primero se
ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por
número: as, 2, 3, 4, 5, 6, 7, sota, caballo, rey.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 16/03/2023
"""
import random
from POO.MeridaVelascoPabloPOOtanda3.ej14deck.card import Card

SUITS = 'bastos copas espadas oros'.split()
NUMBERS = 'as 2 3 4 5 6 7 sota caballo rey'.split()
NUM_CARDS = 10

deck = set()

for _ in range(NUM_CARDS): # TODO Averiguar cómo ordenarlos y recoger posibilidad de que la carta se repita
    card_to_add = Card(random.choice(NUMBERS), random.choice(SUITS))
    deck.add(card_to_add)

cards_list = list(deck)
cards_list.sort(key= lambda c: (c.suit, NUMBERS.index(c.number)))

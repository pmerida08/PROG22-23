"""
14. Crea en Python las siguientes clases:

    Deck que simula un conjunto de cartas de naipes.
        Inicialmente, tiene las cartas que le llegan con el constructor.
        Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
        Le pueden quitar la primera carta (robar).
        Puede barajarse.
    Baraja Española e Inglesa (SpanishDeck e EnglishDeck) que heredan de Deck.


Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 05/03/2023
"""
import random
from typing import List
from typeguard import typechecked

from card import Card


@typechecked
class Deck:

    def __init__(self, cards: List[Card]):
        self.__cards = list(cards)

    @property
    def size(self):
        return len(self.__cards)

    def deal(self, player, number: int):
        if number < 0:
            raise ValueError("El número de cartas a repartir tiene que ser positivo")
        if number > self.size:
            raise ValueError("No hay cartas suficientes para repartir")

        cards_to_deal = self.__cards[:number]
        player.receives(cards_to_deal)
        self.__cards = self.__cards[number:]

    def draw(self):
        if self.size == 0:
            raise ValueError("No quedan cartas en la baraja")
        return self.__cards.pop(0)

    def shuffle(self):
        random.shuffle(self.__cards)

    def __repr__(self):
        return repr(self.__cards)


if __name__ == '__main__':
    cards_ = [
        Card("♣", "4"),
        Card("♣", "6"),
        Card("♡", "2"),
        Card("♡", "3")
    ]

    deck1 = Deck(cards_)
    deck1.shuffle()
    print(deck1)


from typing import List
from typeguard import typechecked
from POO.MeridaVelascoPabloPOOtanda3.ej14deck.card import Card
from POO.MeridaVelascoPabloPOOtanda3.ej14deck.deck import Deck


@typechecked
class HasNotCard(Exception):

    def __init__(self, card):
        super().__init__(f"El jugador no puede deshacerse de la carta {card} porque no la tiene")


class CardPlayer:

    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards.copy()

    def receives(self, cards: List[Card]):
        self.__cards.extend(cards)

    def draws(self, deck: Deck):
        card = deck.draw()
        self.__cards.append(card)

    def throws(self, card: Card):
        if card not in self.__cards:
            raise HasNotCard(card)
        self.__cards.remove(card)

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.__name}, cards={self.__cards})"

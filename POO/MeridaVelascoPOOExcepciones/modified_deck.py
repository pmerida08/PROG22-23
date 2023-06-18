import random
from typing import List
from typeguard import typechecked
from POO.MeridaVelascoPabloPOOtanda3.ej14deck.card import Card


@typechecked
class NotEnoughCards(Exception):
    def __init__(self):
        super().__init__("No hay cartas suficientes para repartir")


class PositiveAmount(Exception):
    def __init__(self, amount):
        super().__init__(f"El número de cartas a repartir (has intentado introducir {amount}) "
                        f"no es válido tiene que ser positivo")


class Deck:

    def __init__(self, cards: List[Card]):
        self.__cards = list(cards)

    @property
    def size(self):
        return len(self.__cards)

    def deal(self, player, number: int):
        if number < 0:
            raise PositiveAmount(number)
        if number > len(self.__cards):
            raise NotEnoughCards()

        cards_to_deal = self.__cards[:number]
        player.receives(cards_to_deal)
        self.__cards = self.__cards[number:]

    def draw(self):
        if self.size == 0:
            raise NotEnoughCards("No quedan cartas en la baraja")
        return self.__cards.pop(0)

    def shuffle(self):
        random.shuffle(self.__cards)

    def __repr__(self):
        return repr(self.__cards)

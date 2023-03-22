"""
Clase de carta para Deck

Card que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de valores).
"""

from dataclasses import dataclass
from typeguard import typechecked


@typechecked
@dataclass(frozen=True)
class Card:
    suit: str
    number: str

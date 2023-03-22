"""
4. Implementar otra clase Dado. Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al
que no se le pasa nada e inicializa el dado al azar, otro al que solo se le pasa que número tiene el dado en la cara
superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el
método roll() que tirará el dado al azar y el __str__(). Implementa un tester que tenga un vector de 4 dados y los lance
una serie de veces.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 15/01/2023
"""
import random
from typing import Optional
from typeguard import typechecked

class OtherDice:

    @typechecked
    def __init__(self, on_top: Optional[int] = None, faces: int = 6):

        if faces <= 0:
            raise ValueError(f'El número de caras no puede ser mayor o igual que 0.')
        elif on_top > faces:
            raise ValueError(f'El número de la cara superior no puede ser superior al del total de caras.')
        else:
            self.__faces = faces

        if on_top is None:
            self.roll()
        else:
            self.__top_face = on_top

    @property
    def top_face(self):
        return self.__top_face

    def roll(self):
        if self.__top_face == 0:
            self.__top_face = random.randint(1, self.__faces)

    def __str__(self):
        return f'La cara que ha salido en el dado con {self.__faces} caras es: {self.__top_face}'

"""
1. Crea una clase "Dado" que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad
de salir y un programa de prueba.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 13/01/2023
"""

import random

class Dice:
    def __init__(self, face = 6):
        self.face = face
    def try_it(self):
        numface = random.randint(1, 6)
        self.face = numface
    def __str__(self):
        dice_number = f'El numero sacado en el dado es el: {self.face}'
        return dice_number

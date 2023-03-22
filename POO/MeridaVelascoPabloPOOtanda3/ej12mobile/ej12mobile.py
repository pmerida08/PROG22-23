"""
12. Implementa la clase Mobile como subclase de Terminal (la clase del ejercicio anterior que ya no hace falta
modificar). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto).
El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede
cambiar. Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada. A continuación
se proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla.
El total tarificado debe aparecer con dos decimales.

Programa principal:

m1 = Mobile("678112233", "rata")
m2 = Mobile("644744469", "mono")
m3 = Mobile("622328909", "bisonte")
print(m1)
print(m2)
m1.call(m2, 320)
m1.call(m3, 200)
m2.call(m3, 550)
print(m1)
print(m2)
print(m3)

Salida:

N.º 678 11 22 33 - 0 s de conversación - tarificados 0,00 euros
N.º 644 74 44 69 - 0 s de conversación - tarificados 0,00 euros
N.º 678 11 22 33 - 520 s de conversación - tarificados 0,52 euros
N.º 644 74 44 69 - 870 s de conversación - tarificados 1,10 euros
N.º 622 32 89 09 - 750 s de conversación - tarificados 0,00 euros

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 05/03/2023
"""
from typeguard import typechecked
from POO.MeridaVelascoPabloPOOtanda3.ej11terminal import Terminal
from rate import Rate


@typechecked
class Mobile(Terminal):

    def __init__(self, number: str, rate: str):
        super().__init__(number)
        self.__rate = Rate(rate)
        self.__price = 0

    @property
    def rate(self):
        return self.__rate.name

    @property
    def price(self):
        return self.__price

    def call(self, other: Terminal, seconds: int):
        super().call(other, seconds)
        self.__price += self.__rate.price(seconds)

    def __str__(self):
        return super().__str__() + f" - tarificados {self.__price:.2f} euros"

if __name__ == '__main__':
    m1 = Mobile("678112233", "rata")
    m2 = Mobile("644744469", "mono")
    m3 = Mobile("622328909", "bisonte")
    print(m1)
    print(m2)
    m1.call(m2, 320)
    m1.call(m3, 200)
    m2.call(m3, 550)
    print(m1)
    print(m2)
    print(m3)
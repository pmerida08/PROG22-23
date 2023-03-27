"""
8. Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito, se
compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo elemento.
Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito. En esta nueva
versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega. El contenido del
programa principal es idéntico al ejercicio anterior.

Salida:

Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Hay 2 productos en la cesta.
El total asciende a 488,90 euros
Continúa la compra...
Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 3 Subtotal: 59,85
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Ahora hay 3 productos en la cesta.
El total asciende a 1105,85 euros

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 27/03/2023
"""
from typeguard import typechecked
@typechecked
class Element:
    def __init__(self, name, price, amount):
        self.__name = name
        self.__price = price * amount
        self.__amount = amount

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def amount(self):
        return self.__amount

@typechecked
class Cart:

    def __init__(self):
        self.elements = list()
        self.number_elements = 0
        self.total_cost = 0

    def add(self, element: Element): # ???
        for e in range(len(self.elements)):
            if element.name in self.elements[e]:
                self.number_elements += element.amount
                self.total_cost += element.price
            else:
                self.elements.append(element)
                self.number_elements += element.amount
                self.total_cost += element.price

    def __str__(self):
        return f"Ahora hay {self.number_elements} productos en la cesta.\n" \
            f"El total asciende a {self.total_cost:.2f}  euros"

    def __repr__(self):
        return f'Número de elementos: {self.number_elements} Total: {self.total_cost:.2f} €.'

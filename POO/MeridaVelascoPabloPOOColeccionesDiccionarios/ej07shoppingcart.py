"""
7. Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra.
Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto, deberás
generar la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la cantidad
(número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal como la
salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal.

Contenido del programa principal:

mi_carrito = Carrito()
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")

print("\nContinúa la compra...\n")
mi_carrito.agrega(Elemento("Samsung Galaxy Tab", 199, 3))
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
print(mi_carrito);
print(f"Ahora hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f}  euros")

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
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Tarjeta SD 64Gb PVP: 19,95 Unidades: 1 Subtotal: 19,95
Ahora hay 4 productos en la cesta.
El total asciende a 1105,85 euros

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 26/03/2023
"""
from typeguard import typechecked

def main():
    mi_carrito = Cart()
    mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 2))
    mi_carrito.add(Element("Canon EOS 2000D", 449, 1))
    print(mi_carrito)
    print(f"Hay {mi_carrito.number_elements} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.total_cost:.2f}  euros")

    print("\nContinúa la compra...\n")
    mi_carrito.add(Element("Samsung Galaxy Tab", 199, 3))
    mi_carrito.add(Element("Tarjeta SD 64Gb", 19.95, 1))
    print(mi_carrito)
    print(f"Ahora hay {mi_carrito.number_elements} productos en la cesta.")
    print(f"El total asciende a {mi_carrito.total_cost:.2f}  euros")

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

    def __repr__(self):
            return f"{self.__name} PVP: {self.__price} Unidades: {self.__amount} \n"

@typechecked
class Cart:

    def __init__(self):
        self.elements = list()
        self.number_elements = 0
        self.total_cost = 0

    def add(self, element: Element):
        if element.name in self.elements:
            self.number_elements += element.amount
            self.total_cost += element.price
        else:
            self.elements.append(element)
            self.number_elements += element.amount
            self.total_cost += element.price

    def __str__(self):
        return f'{self.elements}'

    def __repr__(self):
        return self.elements

if __name__ == '__main__':
    main()



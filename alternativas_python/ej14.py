"""
La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos
A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, esta es de un solo tipo y tamaño, se requiere
determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B,
se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2.
Haz un algoritmo para determinar la ganancia obtenida.

Autor: Pablo Mérida Velasco
Fecha: 16/10/2022
"""

import sys

cantidad = int(input('Indica la cantidad de uva recogida en kilos: '))
tipo = str(input('Indica el tipo de uva: ')).upper()
tamanio = int(input('Indica el tamaño de uva: '))
precio_uva = 0

if tipo == 'A' and tamanio == 1:
    precio_uva = cantidad * 0.2

elif tipo == 'A' and tamanio == 2:
    precio_uva = cantidad * 0.3

elif tipo == 'B' and tamanio == 1:
    precio_uva = cantidad * 0.3

elif tipo == 'B' and tamanio == 2:
    precio_uva = cantidad * 0.5

else:
    print('No coincide con ningun tipo o tamaño dado', file=sys.stderr)
    sys.exit(1)

print(f'El precio de {cantidad} kilos de uva es de: {precio_uva} €')

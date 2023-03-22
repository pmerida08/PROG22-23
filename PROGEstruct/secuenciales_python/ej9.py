"""
9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar
finalmente por su compra.
"""

compra = float(input('Ingresa el coste de la compra del cliente: '))
descuento = (0.15 * compra)

compra_desc = compra - descuento

print('El precio de la compra descontado es de : ', compra_desc)

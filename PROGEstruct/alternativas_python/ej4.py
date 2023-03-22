"""
Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso
en caso contrario.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

print('Division de dos números')

dividendo = int(input('Introduce el valor del dividendo de la división: '))
divisor = int(input('Introduce el valor del divisor de la división: '))

if divisor != 0:
    print(f'El resultado de la división de los dos números es de: {dividendo/divisor}')
else:
    print('El divisor no puede ser 0.')

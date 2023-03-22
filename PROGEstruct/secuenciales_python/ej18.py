"""
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.
"""

nom = str(input("Introduce tu nombre: "))
ap1 = str(input("Introduce tu primer apellido: "))
ap2 = str(input("Introduce el segundo apellido: "))

print('Las iniciales del nombre dado son: ', nom[0] + ap1[0] + ap2[0])


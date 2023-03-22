"""
Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el
superior lo tiene que volver a pedir.

A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes
 informaciones:

 - La suma de los números que están dentro del intervalo (intervalo abierto).
 - Cuantos números están fuera del intervalo.
 - Informa si hemos introducido algún número igual a los límites del intervalo.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""
import sys

minimum = int(input("Introduce el límite inferior: "))
maximum = int(input("Introduce el límite superior: "))
total = 0
outside = 0
same = 0

while minimum > maximum:
    print('Intervalo incorrecto. VUELVE a introducir los valores.')
    minimum = int(input("Introduce el límite inferior: "))
    maximum = int(input("Introduce el límite superior: "))

choice = input("Introduce un número (para acabar introduzca 0): ")

if choice.isalpha():
    print(f'El carácter introducido no puede ser diferente a un número.', file=sys.stderr)
    sys.exit(1)

choice = int(choice)

while choice != 0:
    if maximum < choice < minimum:
        outside += 1
    elif choice == maximum or choice == minimum:
        same += 1
        total += choice
    else:
        total += choice

    choice = int(input("Introduce un número (para acabar introduzca 0): "))

print(f"El total sumado es: {total}.")
print(f"Has introducido {outside} numero fuera del rango.")
print(f"Has introducido {same} numeros iguales a los límites del rango.")

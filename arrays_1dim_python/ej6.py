"""
Ejercicio 6

Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array. El programa
debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los
números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

Autor: Pablo Mérida Velasco
Fecha: 14/11/2022
"""
import random

listed_random = []
listed_pairs = []
listed_impairs = []

for i in range(20):
    random_num = random.randint(0, 100)
    listed_random.append(random_num)

print(f'La lista de la lista sin ordenar es: {listed_random}')
for j in listed_random:
    if j % 2 == 0:
        listed_pairs.append(j)
    else:
        listed_impairs.append(j)

listed_random.clear()
listed_pairs.sort()
listed_impairs.sort()
listed_random.extend(listed_pairs)
listed_random.extend(listed_impairs)

print(f'La lista de la lista ordenada es: {listed_random}')

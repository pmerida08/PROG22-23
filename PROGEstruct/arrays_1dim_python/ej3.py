"""
Ejercicio 3

Define tres arrays de 20 números enteros cada uno, con nombres número, cuadrado y cubo. Carga el array número con
valores aleatorios entre 0 y 100. En el array cuadrado se deben almacenar los cuadrados de los valores que hay en el
array número. En el array cubo se deben almacenar los cubos de los valores que hay en número. A continuación, muestra
el contenido de los tres arrays dispuesto en tres columnas.

Autor: Pablo Mérida Velasco
Fecha: 11/11/2022

"""
import random


number = []
square = []
cube = []

for i in range(21):
    randomized_number = random.randint(0, 101)
    number.append(randomized_number)
    for j in range(21):
        square.append(number[i]**2)
        break
    for k in range(21):
        cube.append(number[i]**3)
        break

print('Numero\t| Cuadrado\t| Cubo')
for p in range(len(number)):
    print(f'{number[p]:7d}\t|\t{square[p]:7d}\t|\t{cube[p]:7d}')

"""
Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno
de estos estados:

- exteriores
- tangentes exteriores
- secantes
- tangentes interiores.
- interiores
- concéntricas

Autor: Pablo Mérida Velasco
Fecha: 15/10/2022
"""
import math

print('Primera circunferencia: ')
x1 = int(input('Introduce la coordenada x1: '))
y1 = int(input('Introduce la coordenada y1: '))
r1 = int(input('Introduce la coordenada r1: '))

print('Segunda circunferencia: ')
x2 = int(input('Introduce la coordenada x2: '))
y2 = int(input('Introduce la coordenada y2: '))
r2 = int(input('Introduce la coordenada r2: '))

distancia = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

if distancia > (r1 + r2):
    print('Son circunferencias exteriores.')
elif distancia == (r1 + r2):
    print('Son circunferencias tangentes exteriores.')
elif (r1 + r2) > distancia > abs(r1 - r2):
    print('Son circunferencias secantes.')
elif distancia == abs(r1 - r2):
    print('Son circunferencias tangentes interiores.')
elif 0 < distancia < abs(r1 - r2):
    print('Son circunferencias interiores.')
elif distancia == 0:
    print('Son circunferencias concéntricas.')
else:
    print('No coinciden ningunos de los parámetros.')

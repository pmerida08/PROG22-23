"""
Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

print('Cálculo de mayor edad entre dos personas.')

persona1 = int(input('Introduce la edad de una persona: '))
persona2 = int(input('Introduce la edad de otra persona: '))

if persona1 > persona2:
    print('La segunda persona es más joven que la primera.')
elif persona1 < persona2:
    print('La priemra persona es más joven que la segunda.')
else:
    print('Las dos personas tienen la misma edad.')

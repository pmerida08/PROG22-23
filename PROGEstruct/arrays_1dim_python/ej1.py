"""
Ejercicio 1

Escribe sentencias Python para realizar cada una de las siguientes tareas:

a) Muestra el valor del elemento 6 de un array f.
b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
c) Total de los 100 elementos de punto-flotante de un array c.
d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
e) Calcula y muestra el valor mayor y menor contenidos en un array W de 99 elementos de punto-flotante

Autor: Pablo Mérida Velasco
Fecha: 11/11/2022

"""
import random

# a) Muestra el valor del elemento 6 de un array f.
f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n' + 'a)')
print(f'El valor de la posición 6 de la lista es de: {f[6]}')

# b) Inicializa los 5 primeros elementos de un array unidimensional de enteros a 8.
array1 = []
for n in range(6):
    array1.append(8)

print('\n' + 'b)')
print(array1)

# c) Total de los 100 elementos de punto-flotante de un array c.
ranging = random.uniform(0.00, 100.00)
c = []
summary = 0
for i in range(101):
    for m in range(101):
        c.append(ranging)
    summary += c[i]

print('\n' + 'c)')
print(f'La suma de los 100 primeros numeros es de: {summary:.2f}')

# d) Copia los 11 elementos de un array a en la primera porción de un array b, el cual contiene 34 elementos.
a = [0] * 11
b = [1] * 34

print('Lista a: ', a)
print('Lista b: ', b)

for o in range(12):
    b.pop(o)

summary2 = a + b

print('\n' + 'd)')
print(summary2)

# e) Calcula y muestra el valor mayor y menor contenidos en un array W de 99 elementos de punto-flotante
w = []

accum = 0
max1 = 0
min1 = 0

for t in range(100):
    ranging2 = random.uniform(0.0, 50.0)
    w.append(ranging2)

print('\n' + 'e)')
print(f'El valor mayor del array W es: ', max(w))
print(f'El valor menor del array W es: ', min(w))

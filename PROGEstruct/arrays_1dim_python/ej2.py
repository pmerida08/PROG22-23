"""
Ejercicio 2

Escribe un programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que
se introduce es el último en mostrarse y viceversa.

Autor: Pablo Mérida Velasco
Fecha: 11/11/2022

"""

listed_num = []
reverse_list = []

for i in range(11):
    num = int(input('Introduce un número: '))
    listed_num.append(num)

listed_num.reverse()

print('La lista al revés es: ', reverse_list)

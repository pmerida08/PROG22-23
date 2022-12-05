"""
Ejercicio 4

Escribe un programa que pida 10 números por teclado y que luego muestre los números introducidos junto con las palabras
“máximo” y “mínimo” al lado del máximo y del mínimo respectivamente.

Autor: Pablo Mérida Velasco
Fecha: 11/11/2022
"""

listed_num = []

for i in range(11):
    num = int(input('Introduce un número: '))
    listed_num.append(num)

listed_num.sort()
print(f'Máximo: {listed_num[-1]}')
print(f'Mínimo: {listed_num[0]}')

"""
Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""

string1 = input('Introduce una cadena por teclado: ')
substring = input('Introduce una subcadena por teclado: ')
is_in = False

for i in range(len(string1) - len(substring) + 1):
    if substring == string1[i:i+len(substring)]:
        is_in = True
        break

if is_in:
    print(f'La cadena -{substring}- está en la cadena -{string1}-')
else:
    print(f'La cadena -{substring}- no está en la cadena -{string1}-')

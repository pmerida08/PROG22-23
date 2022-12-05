"""
Realizar un programa que lea una cadena por teclado y convierta las mayúsculas a minúsculas y viceversa.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""

string = input('Introduce una cadena por teclado: ')
string_converted = []

for i in string:
    if i.isupper():
        i = i.lower()
        string_converted.append(i)
    elif i.islower():
        i = i.upper()
        string_converted.append(i)

new_string = ''.join(string_converted)
print(new_string)

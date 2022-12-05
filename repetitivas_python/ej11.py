"""
Suponiendo que hemos introducido una cadena por teclado que representa una frase (palabras separadas por espacios),
realiza un programa que cuente cuantas palabras tiene.

Autor: Pablo Mérida Velasco
Fecha: 7/11/2022
"""

string1 = input('Introduce una cadena por teclado: ')
string_listed = [n for n in (string1.split(' '))]

print(len(string_listed))

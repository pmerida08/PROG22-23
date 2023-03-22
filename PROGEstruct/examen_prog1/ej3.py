"""
3. Realiza un conversor del sistema decimal al sistema de “palotes”.

Ejemplo:
Por favor, introduzca un número entero positivo: 47021
El 47021 en decimal es el | | | | - | | | | | | | - - | | - | en el sistema de palotes.

Si no se introduce un número entero positivo el programa debe terminar de manera anormal con un
mensaje de error.

Nombre: Pablo Mérida Velasco
Curso: 1DAW A
Fecha: 10/11/2022

"""

print('Este programa pide un número y te lo pone en idioma de palotes.')

# Declaramos las variables
num_dec = int(input('Introduce un número decimal: '))

# Desarrollamos algoritmo
for i in str(num_dec):
    print('|' * int(i) + ' - ', end='')
print('\b\b\b ')

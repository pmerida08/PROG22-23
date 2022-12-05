"""
Realiza un programa que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres
cosas:

    El exponente sea positivo, solo tienes que imprimir la potencia.
    El exponente sea 0, el resultado es 1.
    El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

base = int(input('Introduce la base de una potencia: '))
exponente = int(input('Introduce el exponente de la potencia: '))

if exponente > 0:
    print(f'El resultado de la potencia es de: {base**exponente}')
elif exponente == 0:
    print('El resultado es 0.')
else:
    print(f'El resultado de la potencia es de: {1/(base**(exponente*-1))}')

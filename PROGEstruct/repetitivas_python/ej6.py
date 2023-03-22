"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el
resultado de la potencia. No se puede utilizar el operador de potencia ni la función.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""

print('Este programa hace que dados dos numeros haga su potencia utilizar el operador de la potencia.')
print('----------------------------------------------------------------------------------------------')

base = float(input('Introduce la base de la potencia: '))
exponent = int(input('Introduce el exponente de la potencia: '))
pow_base = base

for i in range(1, exponent):
    pow_base *= base

print(f'La potencia es: {pow_base}')

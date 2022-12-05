"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe
informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

Autor: Pablo Mérida Velasco
Fecha: 26/10/2022
"""

print('Este programa pide una cantidad de numeros, y luego dice la cantidad de ellos si son mayor, menor o '
      'iguales que 0')
print('----------------------------------------------------------------------------------------------------')

numeros_introducidos = int(input('Introduce la cantidad de números a introducir: '))
numero_mayor_0 = 0
numero_menor_0 = 0
numero_igual_0 = 0

for i in range(numeros_introducidos):
    numero = int(input('Introduce un número: '))

    if numero > 0:
        numero_mayor_0 += 1

    if numero < 0:
        numero_menor_0 += 1

    if numero_igual_0 == 0:
        numero_igual_0 += 1

print(f'Hay {numero_mayor_0} números mayores que 0, {numero_menor_0} menores que 0, y {numero_igual_0} iguales que 0.')

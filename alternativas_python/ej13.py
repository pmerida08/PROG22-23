"""
Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.
Hay billetes de 500, 200, 100, 50, 20, 10 y 5 € y monedas de 2 € y 1 €.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente resultado:

    2 billetes de 200 euros.
    1 billete de 20 euros.
    1 billete de 10 euros.
    2 monedas de 2 euros.

Autor: Pablo Mérida Velasco
Fecha: 16/10/2022
"""

dinero = int(input('Introduce el dinero total: '))
print(f'{dinero} € es desglosado en: ')

billetes500 = 0
billetes200 = 0
billetes100 = 0
billetes50 = 0
billetes20 = 0
billetes10 = 0
billetes5 = 0
monedas2 = 0
monedas1 = 0

if dinero // 500:
    billetes500 = dinero // 500
    dinero = dinero % 500

if dinero // 200:
    billetes200 = dinero // 200
    dinero = dinero % 500 % 200

if dinero // 100:
    billetes100 = dinero // 100
    dinero = dinero % 500 % 200 % 100

if dinero // 50:
    billetes50 = dinero // 50
    dinero = dinero % 500 % 200 % 100 % 50

if dinero // 20:
    billetes20 = dinero // 20
    dinero = dinero % 500 % 200 % 100 % 50 % 20

if dinero // 10:
    billetes10 = dinero // 10
    dinero = dinero % 500 % 200 % 100 % 50 % 20 % 10

if dinero // 5:
    billetes5 = dinero // 5
    dinero = dinero % 500 % 200 % 100 % 50 % 20 % 10 % 5

if dinero // 2:
    monedas2 = dinero // 2
    dinero = dinero % 500 % 200 % 100 % 50 % 20 % 10 % 5 % 2

if dinero // 1:
    monedas1 = dinero // 1
    dinero = dinero % 500 % 200 % 100 % 50 % 20 % 10 % 5 % 2 % 1

print(f'{billetes500} billetes de 500 €')
print(f'{billetes200} billetes de 200 €')
print(f'{billetes100} billetes de 100 €')
print(f'{billetes50} billetes de 50 €')
print(f'{billetes20} billetes de 20 €')
print(f'{billetes10} billetes de 10 €')
print(f'{billetes5} billetes de 5 €')
print(f'{monedas2} monedas de 2 €')
print(f'{monedas1} monedas de 1 €')

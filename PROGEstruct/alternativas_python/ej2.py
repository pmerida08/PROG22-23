"""
Realiza el ejercicio 56 (página 100) del libro "Introducción a la Programación con Python 3".

Indica qué líneas del último programa (y en qué orden) se ejecutarán para cada uno
de los siguientes casos:
1) a = 2 y b = 6.
2) a = 0 y b = 3.
3) a = 0 y b = −3.
4) a = 0 y b = 0.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""
a1 = 2
b1 = 6

if a1 > b1:
    print('El mayor es :', a1)
elif a1 < b1:
    print('El mayor es: ', b1)
else:
    print(f'{a1} y {b1} son iguales')

a2 = 0
b2 = 3

if a2 > b2:
    print('El mayor es :', a2)
elif a2 < b2:
    print('El mayor es: ', b2)
else:
    print(f'{a2} y {b2} son iguales')

a3 = 0
b3 = -3

if a3 > b3:
    print('El mayor es :', a3)
elif a3 < b3:
    print('El mayor es: ', b3)
else:
    print(f'{a3} y {b3} son iguales')

a4 = 0
b4 = 0

if a4 > b4:
    print('El mayor es :', a4)
elif a4 < b4:
    print('El mayor es: ', b4)
else:
    print(f'{a4} y {b4} son iguales')

"""
Programa que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor
o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo
sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""

nota = int(input('Introduce la nota: '))
edad = int(input('Introduce la edad: '))
sexo = str(input('Introduce el género: '))

if nota >= 5 and edad >= 18 and sexo[0] == 'F':
    print('ACEPTADA')
elif nota >= 5 and edad >= 18 and sexo[0] == 'M':
    print('POSIBLE')
else:
    print('NO ACEPTADA')

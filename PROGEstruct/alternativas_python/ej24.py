"""
Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la
calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes:
«Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual
que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).

Autor: Pablo Mérida Velasco
Fecha: 20/10/2022
"""

nota = float(input('Introduce un número real: '))
match int(nota):

    case 0 | 1 | 2 | 3 | 4:
        print('Has sacado un SUSPENSO.')
    case 5:
        print('Has sacado un SUFICIENTE.')
    case 6:
        print('Has sacado un BIEN.')
    case 7 | 8:
        print('Has sacado un NOTABLE.')
    case 9:
        print('Has sacado un SOBRESALIENTE.')
    case 10:
        print('Has sacado MATRÍCULA DE HONOR.')
    case _:
        print('No coincide con ningún valor.')

"""
El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno
y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o
más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si
son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realiza un
programa que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.

Autor: Pablo Mérida Velasco
Fecha: 17/10/2022
"""

print('Este programa te calcula el precio por alumno que asistirán al viaje de estudios.')
print('---------------------------------------------------------------------------------')

students = int(input('Introduce la cantidad de alumnos que van a ir al viaje de estudios: '))
cost_students = 0

if students >= 100:
    cost_students = students * 65
    print(f'El costo por alumno es de 65 €, y el total es de: {cost_students} €')
elif 99 > students >= 50:
    cost_students = students * 70
    print(f'El costo por alumno es de 70 €, y el total es de: {cost_students} €')
elif 49 > students >= 30:
    cost_students = students * 95
    print(f'El costo por alumno es de 95 €, y el total es de: {cost_students} €')
else:
    cost_students = 4000
    print(f'El costo por alumno es de: {cost_students} €')

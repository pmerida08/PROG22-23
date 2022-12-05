"""
Ejercicio 5

Realiza un programa que pida la temperatura media que ha hecho en cada mes de un determinado año y que muestre a
continuación un diagrama de barras horizontales con esos datos. Las barras del diagrama se pueden dibujar a base de
asteriscos o cualquier otro carácter.

Autor: Pablo Mérida Velasco
Fecha: 12/11/2022

"""

listed_month = ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct',
                'nov', 'dic']
listed_temp = [] * 12

for i in listed_month:
    temp = int(input(f'Introduce la temperatura que hizo en {i}: '))
    temp *= '*'
    listed_temp.append(temp)

print('\nTemperaturas: ')
for j in range(len(listed_temp)):
    print(f'{listed_month[j]}: {listed_temp[j]} ')

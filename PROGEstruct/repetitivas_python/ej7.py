"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así
sucesivamente. Realizar un programa para determinar cuánto debe pagar mensualmente y el total de lo que pagará después
de los 20 meses.

Autor: Pablo Mérida Velasco
Fecha: 25/10/2022
"""

print('Este programa calcula la cantidad que se tiene que pagar por un producto en los próximos 20 meses.')

MONTHS_PAYMENT = 20
TAX_MONTH = 10

print(f'El primer mes tuvo que pagar por el producto: {TAX_MONTH} €')
for i in range(1, MONTHS_PAYMENT):
    TAX_MONTH += TAX_MONTH
    print(f'El siguiente mes habrá pagado: {TAX_MONTH} €')

print(f'Al final de todos los meses habrá pagado: {TAX_MONTH} €')

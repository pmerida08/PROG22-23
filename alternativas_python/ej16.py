"""
La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que
dura, de tal forma que los primeros cinco minutos cuestan 1 euro por minuto, los siguientes tres, 80 céntimos por
minuto, los siguientes dos minutos, 70 céntimos por minuto, y a partir del décimo minuto, 50 céntimos por minuto.

Además, se carga un impuesto de 3% cuando es domingo, y si es otro día, en turno de mañana, 15%, y en turno de tarde,
10%. Haz un algoritmo para determinar cuánto debe pagar por cada concepto una persona que hace una llamada.

Autor: Pablo Mérida Velasco
Fecha: 17/10/2022
"""

total_time = int(input('Introduce el tiempo de la llamada: '))
day_call = input('Introduce el día de la llamada: ')
day_time = input('Introduce si la llamada ha sido por la mañana o por la tarde: ')
cost_call = 0

if total_time <= 5:
    cost_call = total_time * 100
elif total_time <= 8:
    cost_call = (total_time - 5) * 80 + 500
elif total_time <= 10:
    cost_call = (total_time - 8) * 70 + 240 + 500
else:
    cost_call = (total_time - 10) * 50 + 140 + 240 + 500

match day_call:
    case 'Domingo':
        cost_call += cost_call * 0.03
    case '_':
        if day_time == 'mañana':
            cost_call += cost_call * 0.15
        elif day_time == 'tarde':
            cost_call += cost_call * 0.1

print(f'El coste de la llamada es de: {cost_call/100} €')

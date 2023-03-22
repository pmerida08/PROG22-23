"""

Pide una fecha en formato dd/mm/aaaa del siglo XXI, comprueba si es correcta, en caso de no serlo, señala el
error correspondiente (en el dispositivo de errores) y acaba el programa de forma anormal, en caso de serlo,
muestra el día siguiente a la misma en el mismo formato.

"""
import sys

date = input('Escribe la fecha en formato dd/mm/aaaa, recuerda que tiene que ser a partir del siglo XXI (01/01/2001): ')

day = int(date[:2])
month = int(date[3:5])
year = int(date[6:10])

listed_months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                 'Noviembre', 'Diciembre']

if day < 1:
    print('ERROR. El día no puede ser menor que 1.', file=sys.stderr)
    sys.exit(1)
elif month > 12:
    print('ERROR. El mes no puede ser mayor que 12.', file=sys.stderr)
    sys.exit(2)
elif year < 2001:
    print('ERROR. El año no puede ser menor que 2001.', file=sys.stderr)
    sys.exit(3)
elif year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    if month == 2 and day > 30:
        print(f'ERROR. El mes de {listed_months[month]} tiene hasta 29 días en un año bisiesto.', file=sys.stderr)
        sys.exit(4)
    match month:
        case 2:
            if day == 28:
                day += 1
            elif day == 29:
                day = 1
                month += 1
        case 12:
            if day == 31 and month == 12:
                day = 1
                month = 1
                year += 1
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if day > 31:
                print(f'ERROR. El mes de {listed_months[month]} tiene hasta 31 días'
                      f'año bisiesto.', file=sys.stderr)
                sys.exit(5)
            if day == 30:
                day += 1
            elif day == 31:
                day = 1
                month += 1
        case 4 | 6 | 9 | 11:
            if day > 30:
                print(f'ERROR. El mes de {listed_months[month]} tiene hasta 30 días.', file=sys.stderr)
                sys.exit(6)
            if day == 31:
                day = 1
                month += 1
match month:
    case 12:
        if day == 31 and month == 12:
            day = 1
            month = 1
            year += 1
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        if day > 31:
            print(f'ERROR. El mes de {listed_months[month]} tiene hasta 31 días en un mes .', file=sys.stderr)
            sys.exit(7)
        if day == 30:
            day += 1
        elif day == 31:
            day = 1
            month += 1
    case 4 | 6 | 9 | 11:
        if day > 30:
            print(f'ERROR. El mes de {listed_months[month]} tiene hasta 30 días en un mes .', file=sys.stderr)
            sys.exit(8)
        if day == 31:
            day = 1
            month += 1

date_formatted = f'{day:02d}' + '/' + f'{month:02d}' + '/' + f'{year:04d}'
print(f'El día siguiente es: {date_formatted}')

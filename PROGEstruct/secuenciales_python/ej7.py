# 7. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde

minutos = int(input('Dame una cantidad de minutos: '))

horas = minutos // 60
minutos_c = minutos % 60

print('Los minutos dados en horas y minutos son: ', horas, ' horas y ', minutos_c, ' minutos.')

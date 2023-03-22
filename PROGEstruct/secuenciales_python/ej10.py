"""
10. Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de
los siguientes porcentajes:

* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final.
"""
parcial1 = float(input('Escribe la calificación del primer parcial: '))
parcial2 = float(input('Escribe la calificación del segundo parcial: '))
parcial3 = float(input('Escribe la calificación del tercer parcial: '))
ex_final = float(input('Escribe la calificación del examen final: '))
trabajo_final = float(input('Escribe la calificación del trabajo final: '))

media_parciales = (parcial1 + parcial2 + parcial3)/3

promedio_parciales = media_parciales * 0.55
promedio_ex_final = ex_final * 0.3
promedio_trabajo_final = trabajo_final * 0.15

suma_cal = promedio_parciales + promedio_ex_final + promedio_trabajo_final

print('---------------------------------------------------------------------------------------------------------------')
print('La nota final del alumno es de: ', suma_cal)

"""Se le pide al usuario la hora de salida de la ciudad A en horas, minutos y segundos."""

horaA = float(input("Introduce la hora de salida del ciclista: "))
minutoA = float(input("Introduce los minutos (no puede ser más de 60): "))
segundoA = float(input("Introduce los segundos (no pueden ser más de 60): "))

"""Se le pide al usuario los segundo que tarda el ciclista en llegar a la ciudad B"""

segundosB = float(input("Introduce los segundos que tarda en llegar a la ciudad B"))

"""Para calcular los segundos que tarda de salir de la ciudad A se suman los segundos con los minutos multiplicados
 por 60 y las horas multiplicadas por 3600"""

segundosA = segundoA + (minutoA * 60) + (horaA * 3600)

"""Se restan los segundos entre la ciudad B  la ciudad A y se le hace el valor absoluto para que salga positivo."""

distancia = abs(segundosB - segundosA)

"""Finalmente se divide la distancia por 3600 y por 60 para calcular las horas y los minutos de la llegada a la ciudad B respectivamente.
Después de esto se imprimirán los resultados en horas, minutos y segundos."""

horaB = distancia//3600
minutoB = distancia//60

print("El ciclista tarda: ", horaB, "horas", minutoB, "minutos y", segundosB, "segundos")


"""
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás
viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y
sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más
 rápido al otro.
"""
import sys

print("La velocidad del primer vehículo es mayor que la del segundo.")

speed1 = float(input("Introduce la velocidad en km/h del primer vehículo: "))

speed2 = float(input("Introduce la velocidad en km/h del segundo vehículo: "))
if speed2 >= speed1:
    print('La velocidad del coche 2 no puede ser mayor que la del coche 1', file=sys.stderr)
    sys.exit(1)

distance = float(input("Introduce la distancia en metros del segundo vehículo: "))
if distance <= 0:
    print('La distancia no puede ser menor o igual que 0', file=sys.stderr)
    sys.exit(2)

time = distance * 60 / (speed1 - speed2)

print(f"El coche 1 alcanzará al coche 2 en {time} minutos")

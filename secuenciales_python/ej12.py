"""
Pide al usuario dos pares de números x1,y1 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la
distancia entre ellos.

"""

x1 = float(input("Escribe la primera coordenada de x: "))
y1 = float(input("Escribe la segunda coordenada de x: "))
x2 = float(input("Escribe la primera coordenada de y: "))
y2 = float(input("Escribe la segunda coordenada de y: "))

coordx = (x1 - x2)
coordy = (y1 - y2)

distancia = (coordx, coordy)

print("La distancia entre los puntos dados es de: ", distancia)

"""
Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo que el
resultado sea siempre positivo).
"""

n1 = float(input("Dime un número: "))
n2 = float(input("Dime otro número: "))

distancia = abs(n1 - n2)

print("La distancia de los números es de: ", distancia)

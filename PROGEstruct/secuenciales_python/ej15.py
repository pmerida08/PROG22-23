"""
Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables.
"""

n1 = int(input("Introduce un número: "))
n2 = int(input("Introduce otro número: "))

aux = n1
n1 = n2
n2 = aux

# n1, n2 = n2, n1 (Intercambiar valores en python más facil)

print("El valor del primer número es: ", n1)
print("El valor del segundo número es de: ", n2)

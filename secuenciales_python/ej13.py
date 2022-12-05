"""
Realiza un programa que lea un número y que muestre su raíz cuadrada y su raíz cúbica. Python no tiene ninguna función
predefinida que permita calcular la raíz cúbica, ¿cómo se puede calcular?
"""

n1 = float(input("Dime un número: "))

rcuadrada = n1**1//2
rcubica = n1**1//3

print("La raíz cuadrada del número es: ", rcuadrada)
print("La raíz cúbica del número es: ", rcubica)

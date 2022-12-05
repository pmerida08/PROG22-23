"""
2. Nos podemos aproximar al número PI usando la serie de Leibniz que dice que PI se puede
obtener a partir de la siguiente sucesión: 4/1 – 4/3 + 4/5 – 4/7 + 4/9...

Si te fijas, el 4 (numerador) es fijo, y el denominador se aumenta de 2 en 2. Además, en cada paso
se intercambia el signo.

Haz un programa que pidiendo el número de iteraciones nos del valor de PI.

Nombre: Pablo Mérida Velasco
Curso: 1DAW A
Fecha: 10/11/2022

"""

print('Este programa calcula el número PI mediante la serie de Leibniz.')

# Declaramos las variables
NUM = 4
denom = 1
new_operation = 0
iterations = int(input('Indica el número de iteraciones que quieres que tenga para calcular PI: '))

# Desarrollamos el algoritmo
for i in range(iterations):
    operation = -(NUM/denom)
    if i % 2 == 0:
        operation *= -1
    denom += 2
    new_operation += operation

print(new_operation)

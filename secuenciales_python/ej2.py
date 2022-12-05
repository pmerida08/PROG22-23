# 2. Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = int(input('Dime la base del rectángulo: '))
altura = int(input('Dime la altura del rectángulo: '))

perimetro = 2 * base + 2 * altura
area = base * altura

print('El perímetro del rectángulo es: ', perimetro)
print('El área del rectángulo es: ', area)

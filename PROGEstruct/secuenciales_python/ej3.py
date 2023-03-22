# 3. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
from math import sqrt

c1 = int(input('Dime el lado de un cateto del triángulo: '))
c2 = int(input('Dime el lado de otro cateto del triángulo: '))

hipotenusa = sqrt(c1**2 + c2**2)
print('El valor de la hipotenusa: ', hipotenusa)

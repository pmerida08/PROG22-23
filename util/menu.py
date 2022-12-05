# Este programa despliega un menu que da lugar a varias acciones

import sys

print('Menu: ')
print('1. Opcion' + '\n'
      '2. Opcion' + '\n'
      '3. Opcion' + '\n'
      '4. Opcion' + '\n'
      '5. Salir')
print('---------------------------------------------------------------------------------------------------------------')

# El método "match" funciona a partir de Python 3.10
while True:
    opcion = int(input('Introduce la acción que desee hacer: '))
    match opcion:
        case 1:
            print('Has elegido la opción 1')
        case 2:
            print('Has elegido la opción 2')
        case 3:
            print('Has elegido la opción 3')
        case 4:
            print('Has elegido la opción 4')
        case 5:
            print('Has salido del programa con éxito.', file=sys.stderr)
            sys.exit(1)
        case _:
            print('La opcion no es correcta')
            break

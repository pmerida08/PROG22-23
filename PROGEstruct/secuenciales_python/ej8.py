"""
8. Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero
 obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando
  en cuenta su sueldo base y comisiones
"""

sueldo_base = float(input('El sueldo base del vendedor es de: '))

comision = sueldo_base * 0.1
aniadido = sueldo_base + (comision * 3)

print('El total de salario que recibe al mes el vendedor es de: ', aniadido)

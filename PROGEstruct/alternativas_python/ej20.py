"""
Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central,
América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la
que va dirigido. Lo anterior se muestra en la tabla:
ZONA	UBICACIÓN	COSTO/GRAMO
1	América del Norte	24.00 euros
2	América Central	20.00 euros
3	América del Sur	21.00 euros
4	Europa	10.00 euros
5	Asia	18.00 euros

Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de
logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el
rechazo de la entrega.

Autor: Pablo Mérida Velasco
Fecha: 18/10/2022
"""

import sys

peso_paquete = int(input('Introduce el peso del paquete (en gramos): '))
zona_dirigida = input('Introduce la zona a la que va dirigida el paquete: ')

if peso_paquete > 5000:
    print('El paquete no puede pesar más de 5 kg', file=sys.stderr)
    sys.exit(1)

match zona_dirigida:
    case 'América del Norte':
        costo_paquete = peso_paquete * 24
        print(f'El coste del transporte del paquete a {zona_dirigida} es de: {costo_paquete} €')
    case 'América Central':
        costo_paquete = peso_paquete * 20
        print(f'El coste del transporte del paquete a {zona_dirigida} es de: {costo_paquete} €')
    case 'América del Sur':
        costo_paquete = peso_paquete * 21
        print(f'El coste del transporte del paquete a {zona_dirigida} es de: {costo_paquete} €')
    case 'Europa':
        costo_paquete = peso_paquete * 10
        print(f'El coste del transporte del paquete a {zona_dirigida} es de: {costo_paquete} €')
    case 'Asia':
        costo_paquete = peso_paquete * 18
        print(f'El coste del transporte del paquete a {zona_dirigida} es de: {costo_paquete} €')
    case '_':
        print(f'{zona_dirigida} no vale como zona de transporte para el paquete.', file=sys.stderr)
        sys.exit(2)

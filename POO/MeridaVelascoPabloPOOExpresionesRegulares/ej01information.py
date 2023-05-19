"""
1. Programa que recibe dos parámetros: un fichero de texto y una cadena que le indica qué información va a extraer del
mismo, después muestra por la pantalla los datos extraídos.

Los posibles valores del segundo parámetro y la información que extrae es:

    - DNI: extrae los DNI.
    - IP: extrae las direcciones IP.
    - MAT: extrae matrículas de coche con formato 0000XXX.
    - HEX: extrae números hexadecimales. Entendemos que las letras entre A y F son en mayúsculas y el número empieza
    con #.
    - FEC: extrae fechas con formato dd/mm/aaaa.
    - TWT: extrae usuarios de twitter: empieza por @ y puede contener letras mayusculas y minusculas, numeros, guiones
    y guiones bajos.

El programa tiene que ser en relación con su complejidad y número de líneas lo más eficiente posible.

"""

import re
import sys


def extract_info(file, info):
    try:
        regex = {
            'DNI': r'\d{8}[A-HJ-NP-TV-Z]',
            'IP': r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+',
            'MAT': r'\d{4}[A-Z]{3}',
            'HEX': r'#[0-9A-F]{3}',
            'FEC': r'[0-9]{2}/[0-9]{2}/[0-9]{4}',
            'TWT': r'@\w{,15}'
        }

        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
            info = re.findall(regex[info], text)  # DNIs

            for item in info:
                print(item)

    except FileNotFoundError:
        print('El archivo no se ha encontrado.')


if __name__ == '__main__':
    name_file = sys.argv[1]
    info_type = sys.argv[2]
    extract_info(name_file, info_type)

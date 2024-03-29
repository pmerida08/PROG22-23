"""
2. Programa que reciba una url y el nombre de una etiqueta html. Si la url es válida debe mostrar por la pantalla el
contenido de cada etiqueta.

Ejemplo:

si ejecuto python miprograma https://www.iesgrancapitan.org/ title

La salida sería:

Centro Educativo IES Gran Capitán

Número de etiquetas encontradas: 1

ó si ejecuto python miprograma https://example.com/ p

La salida sería:

This domain is for using in illustrative examples in documents. You may use this domain in literature without prior
coordination or asking for permission.

<a href="https://www.iana.org/domains/example">More information...</a>

Número de etiquetas encontradas: 2

"""
import re
import sys
import requests
from requests import RequestException


def main():

    source_code = extract_code()

    tag = sys.argv[2]
    check_args()

    pattern = f'<{tag}>(.*?)</{tag}>'
    results = re.findall(pattern, source_code, re.DOTALL)
    for e in results:
        print(e + '\n')
    print(f'Número de etiquetas encontradas: {len(results)}')


def extract_code():
    try:
        url = sys.argv[1]
        response = requests.get(url)
        return response.text

    except RequestException:
        print('La conexión o la url son erróneas', file=sys.stderr)
        sys.exit(1)


def check_args():
    if len(sys.argv) == 3:
        return
    else:
        print("Error en el número de argumentos. La sintaxis correcta es <URL> <ETIQUETA HTML>", file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()

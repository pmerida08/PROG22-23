"""
4. Escribe un programa capaz de quitar los comentarios de un programa de Java.

Se utilizaría de la siguiente manera:

python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:

python quita-comentarios.py HolaV1.java HolaV2.java

Crea un fichero con nombre HolaV2.java que contiene el código de HolaV1.java pero sin los comentarios.

"""
import sys

origin_file = sys.argv[1]
new_file = sys.argv[2]

with open(origin_file, 'r', encoding='utf-8') as file:
    file_str = file.read()

    while True:
        n1 = file_str.find('//')
        if n1 == -1:
            break
        n2 = file_str.find('\n', n1)
        if n2 == -1:
            file_str = file_str[:n1]
        else:
            file_str = file_str[:n1] + file_str[n2:]

    while True:
        n1 = file_str.find('/*')
        if n1 == -1:
            break
        n2 = file_str.find('*/', n1)
        if n2 == -1:
            file_str = file_str[:n1]
        else:
            file_str = file_str[:n1] + file_str[n2:]

with open(new_file, 'w+', encoding='utf-8') as file:
    new_str = file.write(file_str)

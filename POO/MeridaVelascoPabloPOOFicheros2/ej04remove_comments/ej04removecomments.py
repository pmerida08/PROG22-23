"""
4. Escribe un programa capaz de quitar los comentarios de un programa de Java.

Se utilizaría de la siguiente manera:

python quita-comentarios.py <PROGRAMA_ORIGINAL> <PROGRAMA_LIMPIO>

Por ejemplo:

python quita-comentarios.py Holav1.java Holav2.java

Crea un fichero con nombre Holav2.java que contiene el código de Holav1.java pero sin los comentarios.

"""

ORIGIN_FILE = 'Holav1.java'
NEW_FILE = 'Holav2.java'

with open(ORIGIN_FILE, 'r+t', encoding='utf-8') as file:
    lines = file.readlines()



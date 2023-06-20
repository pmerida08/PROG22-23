"""
2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también
pasamos como parámetro, de manera que:

    - Si el programa no recibe el número de parámetros adecuado termina con un error 1.
    - Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
    antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
    - Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
    código 2.
    - Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina con un
    mensaje de error y código 3.
    - Para encriptar usa el método César, necesitarás una clave que debes pedir al usuario.
"""
import sys

LEN_ALPHABET = 26


class EncryptLenValueError(Exception):
    def __init__(self):
        super().__init__('La clave no puede ser mayor que 26')


def encrypt(msg, keyname):
    encrypted_msg = ""
    for char in msg:
        if char.isalpha():
            new_char_code = ord(char.upper()) + keyname
            if new_char_code > ord('Z'):
                new_char_code -= LEN_ALPHABET
            encrypted_msg += chr(new_char_code)
        else:
            encrypted_msg += char
    return encrypted_msg


if len(sys.argv) > 3:
    print("Error: número de parámetros incorrecto.")
    sys.exit(1)

try:
    key = int(input("Introduce la clave de encriptación: "))
    if key > 26:
        raise EncryptLenValueError()
except ValueError:
    print("Error: la clave debe ser un número entero.")
    sys.exit(1)
except EncryptLenValueError:
    print("Error: la clave no puede ser mayor que 26.")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as f:
        decrypted = f.read()
except FileNotFoundError:
    print("Error: el archivo origen no existe")
    sys.exit(2)
except IOError:
    print("Error: no se puede abrir el archivo origen")
    sys.exit(2)

encrypted_message = encrypt(decrypted, key)

try:
    if len(sys.argv) == 2:
        encrypted_file = sys.argv[1]
        with open(encrypted_file, "w") as f:
            f.write(encrypted_message)
    if len(sys.argv) == 3:
        encrypted_file = sys.argv[2]
        with open(encrypted_file, "w") as f:
            f.write(encrypted_message)
except IOError:
    print("Error: no se puede escribir en el archivo destino")
    sys.exit(3)

print("Archivo encriptado con éxito.")

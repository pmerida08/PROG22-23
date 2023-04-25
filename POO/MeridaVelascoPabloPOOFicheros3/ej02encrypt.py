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


def encrypt(msg, keyname):
    encrypted_msg = ""
    for char in msg:
        if char.isalpha():
            new_char_code = ord(char.upper()) + keyname
            if new_char_code > ord('Z'):
                new_char_code -= 26
            encrypted_msg += chr(new_char_code)
        else:
            encrypted_msg += char
    return encrypted_msg

key = int(input("Introduce la clave de encriptación: "))

try:
    with open(sys.argv[1], "r") as f:
        message = f.read()
except FileNotFoundError:
    print("Error: el archivo origen no existe")
    sys.exit(2)
except IOError:
    print("Error: no se puede abrir el archivo origen")
    sys.exit(2)

encrypted_message = encrypt(message, key)

if len(sys.argv) == 2:
    answer = input("El archivo origen será sobrescrito. ¿Desea continuar? (s/n)")
    if answer.lower() != "s":
        sys.exit()

try:
    with open(sys.argv[2], "w") as f:
        f.write(encrypted_message)
except IndexError:
    with open(sys.argv[1], "w") as f:
        f.write(encrypted_message)
except IOError:
    print("Error: no se puede escribir en el archivo destino")
    sys.exit(3)

print("Archivo encriptado con éxito.")
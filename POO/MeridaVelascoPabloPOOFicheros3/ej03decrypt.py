"""
3. Haz un programa que reciba como parámetro un fichero encriptado con el método César, lo desencripte y almacene el
resultado en otro archivo, que también pasamos como parámetro, de manera que:

    - Si el programa no recibe el número de parámetros adecuado termina con un error 1.
    - Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
    antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
    - Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
    código 2.
    - Si en el fichero destino no se puede escribir (da error al abrirlo como escritura) el programa termina con un
    mensaje de error y código 3.
    - Para desencriptar necesitas una clave que debes pedir al usuario.
    - ¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves...
    ¡impleméntala!
"""

import sys

def decrypt(encrypted_msg, keyname):
    decrypted_msg = ""
    for char in encrypted_msg:
        if char.isalpha():
            new_char_code = ord(char.upper()) - keyname
            if new_char_code < ord('A'):
                new_char_code += 26
            decrypted_msg += chr(new_char_code)
        else:
            decrypted_msg += char
    return decrypted_msg

if len(sys.argv) not in (2, 3):
    print("Uso: python decrypt.py fichero_encriptado [fichero_destino]")
    sys.exit(1)

key = int(input("Introduce la clave de desencriptación: "))

try:
    with open(sys.argv[1], "r") as f:
        encrypted_message = f.read()
except FileNotFoundError:
    print("Error: el archivo encriptado no existe")
    sys.exit(2)
except IOError:
    print("Error: no se puede abrir el archivo encriptado")
    sys.exit(2)

decrypted_message = decrypt(encrypted_message, key)

if len(sys.argv) == 2:
    answer = input("El archivo encriptado será sobrescrito. ¿Desea continuar? (s/n)")
    if answer.lower() != "s":
        sys.exit()

try:
    with open(sys.argv[2], "w") as f:
        f.write(decrypted_message)
except IndexError:
    with open(sys.argv[1], "w") as f:
        f.write(decrypted_message)
except IOError:
    print("Error: no se puede escribir en el archivo destino")
    sys.exit(3)

print("Archivo desencriptado con éxito.")
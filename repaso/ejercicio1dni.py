"""
Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y la letra es correcta.
Para calcular la letra se divide el número entre 23 y el resto indica la posición de la cadena de letras:
"TRWAGMYFPDXBNJZSQVHLCKE"

"""
import sys

while True:
    dni = input('Escribe tu dni: ')
    num_dni = dni[:8]
    alpha_dni = dni[8:9]
    string_letters = 'TRWAGMYFPDXBNJZSQVHLCKE'

    if not len(dni) == 9 or not num_dni.isdigit() or not alpha_dni.isalpha() or not alpha_dni.isupper():
        print('ERROR. El formato del DNI es inválido.', file=sys.stderr)
        sys.exit(1)
    else:
        break

position = int(num_dni) % 23

if alpha_dni == string_letters[int(position)]:
    print('Es correcto el DNI.')
else:
    print('Es incorrecto el DNI.')

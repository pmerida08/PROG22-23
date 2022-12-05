"""
Diseña un programa que lea un carácter de teclado y muestre por pantalla el mensaje «Es signo de puntuación» solo si el
carácter leído es un signo de puntuación, «Es una letra» si es una letra (da igual que sea mayúscula, minúscula o
acentuada), «Es un dígito» si es un dígito, «Es otro carácter» si no es ninguno de los anteriores y «No es un carácter»
si el usuario ha introducido más de un carácter.

Pista: quizás te pueda venir bien usar el método find de la clase str.

Autor: Pablo Mérida Velasco
Fecha: 14/10/2022
"""
MARCAS_PUNTUACION = ',;.:...?¿!¡'

char = input('Introduce una frase: ')

# Mirar metodo find() en libro_python.pdf

if len(char) == 1:
    if MARCAS_PUNTUACION in char:
        print('Es signo de puntuación.')
    elif char.isalpha():
        print('Es una letra.')
    elif char.isdigit():
        print('Es un número.')
    else:
        print('No es ningún carácter.')
else:
    print(f'La cadena {char} tiene más de un carácter.')

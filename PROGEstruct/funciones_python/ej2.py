"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función es_capicua() resulta trivial teniendo voltea() y la función siguiente_primo() también es muy
fácil de implementar teniendo es_primo().

Prohibido utilizar funciones de conversión del número a una cadena.

    - es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.

    - es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.

    - siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.

    - digitos: devuelve el número de dígitos de un número entero.

    - voltea: le da la vuelta a un número.

    - digito_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de
    izquierda a derecha.

    - posicion_de_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se
    encuentra, devuelve -1.

    - quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).

    - quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).

    - pega_por_detras: añade un dígito a un número por detrás.

    - pega_por_delante: añade un dígito a un número por delante.

    - trozoDeNumero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo
    correspondiente.

    - juntaNumeros: pega dos números para formar uno.


Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

Autor: Pablo Mérida Velasco
Fecha: 08/12/2022
"""
from math import sqrt


def digitos(x):
    counter = 0

    while True:
        counter += 1
        if x < 0:
            x = x // -10
        x = x // 10
        if x == 0:
            break
    return counter


def es_primo(x):
    primo = False
    divisor = 2

    while divisor <= sqrt(x) and not primo:
        if x % divisor == 0:
            return False
        divisor += 1
        return True


def posicion_de_digito(x):

    pass


def voltea(x):
    pass


if __name__ == '__main__':
    num = int(input('Introduce un número: '))
    print(f'Número de dígitos: {digitos(num)}')
    print(f'Es primo: {es_primo(num)}')
    print(f'Número dado la vuelta: {voltea(num)}')

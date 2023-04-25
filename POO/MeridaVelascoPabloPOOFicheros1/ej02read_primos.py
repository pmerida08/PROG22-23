"""
2. Escribe un programa que sea capaz de leer el fichero anterior y lo muestre por la pantalla.

Autor: Pablo Mérida Velasco
Curso: 1º DAW A
Fecha: 05/04/2023
"""

def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

primes_numbers = []

for n in range(1, 501):
    if is_prime(n):
        primes_numbers.append(n)

with open('D:\Programas\PROG\POO\MeridaVelascoPabloPOOFicheros1\primos.txt', 'wt') as file:
    for line in primes_numbers:
        file.write(str(line) + '\n')

with open('D:\Programas\PROG\POO\MeridaVelascoPabloPOOFicheros1\primos.txt', 'rt') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

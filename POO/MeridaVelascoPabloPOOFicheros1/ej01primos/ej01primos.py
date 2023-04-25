"""
1. Escribe un programa que guarde en un fichero con nombre primos.txt los números primos que hay entre 1 y 500.

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

with open('D:\Programas\PROG\POO\MeridaVelascoPabloPOOFicheros\ej01primos\primos.txt', 'w') as file:
    for line in primes_numbers:
        file.write(str(line) + '\n')

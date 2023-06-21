"""
Haz el ejercicio 1 usando una función generadora.

    Programa ej03.py
    Autor: Pablo Mérida Velasco
    Fecha: 14/05/2023
"""

import math
from typeguard import typechecked


@typechecked
def prime_generator(stop: int):
    if stop < 2:
        raise ValueError("El máximo debe ser mayor o igual a 2")
    prime = 2
    while prime <= stop:
        yield prime
        prime = next_prime(prime)


def next_prime(num: int):
    if num == 2:
        return 3
    candidate_prime = num + 2
    while not is_prime(candidate_prime):
        candidate_prime += 2
    return candidate_prime


def is_prime(num):
    for i in range(3, int(math.sqrt(num) + 1), 2):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for p in prime_generator(15):
        print(p, end=" ")

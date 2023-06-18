"""
    1. Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado
    como máximo.

        Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
"""
import math
from typing import Iterator


class PrimeIterator(Iterator):
    def __init__(self, stop):
        if stop < 2:
            raise ValueError('El mínimo debe ser mayor o igual que 2')
        self.__stop = stop
        self.__current_prime = 2

    def __next__(self):
        if self.__current_prime > self.__stop:
            raise StopIteration
        prime, self.__current_prime = self.__current_prime, self.__next_prime()
        return prime

    def __next_prime(self):
        if self.__current_prime == 2:
            return 3
        candidate_prime = self.__current_prime + 2
        while not self.__is_prime(candidate_prime):
            candidate_prime += 2
        return candidate_prime

    @staticmethod
    def __is_prime(num):
        for i in range(3, int(math.sqrt(num) + 1), + 2):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    num_limit = int(input('Introduce hasta qué valor desea sacar la lista de números primos: '))
    for p in PrimeIterator(num_limit):
        print(p, end=" ")
    print()

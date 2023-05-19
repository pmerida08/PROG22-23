"""
    1. Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado
    como máximo.

        Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
"""
from typing import Iterator


class PrimeIterator(Iterator):
    def __init__(self, nums):
        self.__nums = nums

    def __next__(self):
        nums = [n for n in range(2, 20)]
        for _ in nums:
            primes = list(filter(lambda x: self.es_primo(x), self.__nums))
            return primes

    @staticmethod
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def __str__(self):
        return str(self.__nums)


if __name__ == '__main__':
    pr1 = list(PrimeIterator(15))
    print(pr1)

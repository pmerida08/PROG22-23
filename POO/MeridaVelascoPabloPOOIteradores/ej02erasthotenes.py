"""
2. Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de
Eratóstenes.

"""
from typing import Iterator
from typeguard import typechecked


@typechecked
class PrimeIterator(Iterator):

    @staticmethod
    def is_mult(num, mult):
        return num % mult == 0

    def __init__(self, last_number: int = 20):
        self.__last_number = last_number
        self.__num_primes = self.__sieve_etatostenes(last_number)
        self.__primes_iterator = iter(self.__num_primes)

    @staticmethod
    def __sieve_etatostenes(stop):
        primes = list(n for n in range(2, stop + 1))
        index = 0

        while primes[index] ** 2 < stop:
            for j in range(len(primes[index+1:])):

                index += 1
        return primes

    def __next__(self):
        return next(self.__primes_iterator)

    def __str__(self):
        return str(self.__num_primes)


if __name__ == '__main__':
    prime = PrimeIterator()
    print(prime)

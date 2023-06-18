"""
2. Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de
Eratóstenes.

"""
from typing import Iterator
from typeguard import typechecked


@typechecked
class PrimeIterator(Iterator):

    def __init__(self, last_number: int = 20):
        num_primes = self.__sieve_eratosthenes(last_number)
        self.__primes_iterator = iter(num_primes)

    @staticmethod
    def is_mult(num, mult):
        return num % mult == 0

    @staticmethod
    def __sieve_eratosthenes(stop):
        primes = list(range(2, stop + 1))
        index = 0

        while primes[index] ** 2 < stop:
            for num in primes[index+1:]:
                if num % primes[index] == 0:
                    primes.remove(num)

            index += 1
        return primes

    def __next__(self):
        return next(self.__primes_iterator)


if __name__ == '__main__':
    num_limit = int(input('Introduce hasta qué valor desea sacar la lista de números primos: '))
    for p in PrimeIterator(num_limit):
        print(p, end=" ")
    print()

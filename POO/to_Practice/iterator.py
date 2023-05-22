from typing import Iterator


class NumIterator(Iterator):
    def __init__(self):
        self.__nums = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024)
        self.__index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__index >= len(self.__nums):
            raise StopIteration
        n = self.__nums[self.__index]
        self.__index += 1
        return n

    def __str__(self):
        return f"NumIterator: current index - {self.__index}"


if __name__ == '__main__':
    iterator = NumIterator()
    for num in iterator:
        print(num)

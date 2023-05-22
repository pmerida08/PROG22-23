def mult_generator(n):
    for i in range(1, 11):
        yield i*n


for x in mult_generator(8):
    print(x)

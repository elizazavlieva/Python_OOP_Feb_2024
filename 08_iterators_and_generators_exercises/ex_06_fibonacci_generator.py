def fibonacci():
    first, second = 0, 1

    while True:

        yield first

        first, second = second, first + second


""" TESTS """
generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))


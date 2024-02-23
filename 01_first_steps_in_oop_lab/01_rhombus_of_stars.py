def print_triangle(n, el):
    print(" " * (n - el), end="")
    print(*["*"] * el)


def first_half(n):
    for el in range(1, n + 1):
        print_triangle(n, el)


def second_half(n):
    for el in range(n-1, 0, -1):
        print_triangle(n, el)


def create(n):
    first_half(n)
    second_half(n)


create(int(input()))
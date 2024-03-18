def genrange(start: int, end: int):
    temp_value = start
    while temp_value <= end:
        yield temp_value
        temp_value += 1


print(list(genrange(1, 10)))

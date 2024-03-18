class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.temp_variable = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.temp_variable += 1
        if self.temp_variable <= self.end:
            return self.temp_variable
        raise StopIteration


"""TESTS"""
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)

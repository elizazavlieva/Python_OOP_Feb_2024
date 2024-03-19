class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count - 1 > self.iterations:
            self.iterations += 1
            return self.iterations * self.step
        raise StopIteration

"""TEST"""
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

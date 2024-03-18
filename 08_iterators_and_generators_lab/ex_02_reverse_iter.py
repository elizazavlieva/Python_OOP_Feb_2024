class reverse_iter:
    def __init__(self, info: list):
        self.info = info
        self.index = len(self.info)
        self.end = 0

    def __iter__(self):
        return reversed(self.info)

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.index -= 1
    #     if self.index >= self.end:
    #         return self.info[self.index]
    #     raise StopIteration


"""TEXT"""

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


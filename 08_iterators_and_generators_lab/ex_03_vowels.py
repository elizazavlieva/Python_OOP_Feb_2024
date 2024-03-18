class vowels:
    def __init__(self, my_string: str):
        self.my_string = my_string
        self.vowels = ["a", "e", "i", "u", "y", "o"]
        self.index = -1
        self.string_vowels = [char for char in self.my_string if char.lower() in self.vowels]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.string_vowels):
            return self.string_vowels[self.index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

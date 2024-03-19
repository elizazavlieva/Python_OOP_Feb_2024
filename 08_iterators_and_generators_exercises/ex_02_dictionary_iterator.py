class dictionary_iter:
    def __init__(self, dict_obj: dict):
        self.dict_obj = dict_obj
        self.list_obj = list(dict_obj.items())
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self.list_obj):
            return self.list_obj[self.index]
        raise StopIteration


""" TESTS """
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)


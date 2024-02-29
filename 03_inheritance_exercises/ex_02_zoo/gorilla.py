from ex_02_zoo.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        super().__init__(name)
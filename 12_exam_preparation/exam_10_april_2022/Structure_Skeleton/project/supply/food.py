from project.supply.supply import Supply


class Food(Supply):
    ENERGY = 25

    def __init__(self, name: str, energy: int = 25):
        super().__init__(name, energy)

    def details(self):
        if type(self).__name__ in self.SUPPLY_TYPES:
            return f"{type(self).__name__}: {self.name}, {self.energy}"
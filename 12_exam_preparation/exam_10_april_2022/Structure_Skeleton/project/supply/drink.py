from project.supply.supply import Supply


class Drink(Supply):
    ENERGY = 15

    def __init__(self, name: str, energy: int = 15):
        super().__init__(name, energy)

    def details(self):
        if type(self).__name__ in self.SUPPLY_TYPES:
            return f"{type(self).__name__}: {self.name}, {self.energy}"

from project.supply.supply import Supply


class Player:
    MIN_STAMINA = 0
    MAX_STAMINA = 100
    PLAYERS_NAMES = []

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def need_sustenance(self):
        return self.stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in self.PLAYERS_NAMES:
            raise Exception(f"Name {value} is already used!")

        self.__name = value
        self.PLAYERS_NAMES.append(value)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < self.MIN_STAMINA or value > self.MAX_STAMINA:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def increase_stamina(self, supply: Supply):
        result = self.stamina + supply.energy
        self.stamina = self.MAX_STAMINA if result >= self.MAX_STAMINA \
            else result

    def reduce_stamina(self):
        result = self.stamina - (self.age * 2)
        self.stamina = result if self.stamina - (self.age * 2) >= self.MIN_STAMINA else 0

    def check_player_stamina(self):
        return self.stamina == 0

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

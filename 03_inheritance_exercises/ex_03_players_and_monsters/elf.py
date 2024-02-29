from ex_03_players_and_monsters.hero import Hero


class Elf(Hero):
    def __str__(self):
        return f"{self.username} of type {Elf.__name__} has level {self.level}"
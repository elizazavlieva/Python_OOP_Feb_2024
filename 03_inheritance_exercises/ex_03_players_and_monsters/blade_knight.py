from ex_03_players_and_monsters.dark_knight import DarkKnight


class BladeKnight(DarkKnight):
    def __str__(self):
        return f"{self.username} of type {BladeKnight.__name__} has level {self.level}"
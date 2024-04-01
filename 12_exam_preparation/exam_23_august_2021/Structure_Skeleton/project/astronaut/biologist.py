from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXY_UNITS = 70
    OXYGEN_BREATHING = 5

    def __init__(self, name):
        super().__init__(name, self.OXY_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_BREATHING

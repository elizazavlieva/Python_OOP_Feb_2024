from project.astronaut.astronaut import Astronaut


class Meteorologist (Astronaut):
    OXY_UNITS = 90
    OXYGEN_BREATHING = 15

    def __init__(self, name):
        super().__init__(name, self.OXY_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_BREATHING

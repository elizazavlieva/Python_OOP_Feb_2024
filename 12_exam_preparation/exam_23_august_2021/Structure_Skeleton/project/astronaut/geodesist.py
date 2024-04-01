from project.astronaut.astronaut import Astronaut


class Geodesist (Astronaut):
    OXY_UNITS = 50

    def __init__(self, name):
        super().__init__(name, self.OXY_UNITS)

    def breathe(self):
        self.oxygen -= self.OXYGEN_BREATHING

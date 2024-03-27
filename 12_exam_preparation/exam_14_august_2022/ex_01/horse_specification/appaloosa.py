from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED = 2

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + self.SPEED > self.MAX_SPEED \
            else self.SPEED + self.speed

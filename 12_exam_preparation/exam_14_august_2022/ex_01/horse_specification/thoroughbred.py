from project.horse_specification.horse import Horse


class Thoroughbred (Horse):
    MAX_SPEED = 140
    SPEED = 3

    def train(self):
        self.speed = self.MAX_SPEED if self.speed + self.SPEED > self.MAX_SPEED \
            else self.SPEED + self.speed


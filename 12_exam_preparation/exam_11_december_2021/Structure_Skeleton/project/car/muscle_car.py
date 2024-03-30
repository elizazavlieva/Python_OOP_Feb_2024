from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value < self.MIN_SPEED_LIMIT or value > self.MAX_SPEED_LIMIT:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!")
        self.__speed_limit = value



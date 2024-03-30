from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    CARE_TYPES = {"MuscleCar": MuscleCar,
                  "SportsCar": SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.CARE_TYPES:
            return
        if model in [x.model for x in self.cars]:
            raise Exception(f"Car {model} is already created!")

        self.cars.append(self.CARE_TYPES[car_type](model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if driver_name in [x.name for x in self.drivers]:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if race_name in [x.name for x in self.races]:
            raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.get_driver(driver_name)
        if car_type not in self.CARE_TYPES:
            return
        cars = [x for x in self.cars if type(x).__name__ == car_type and not x.is_taken]
        if not cars:
            raise Exception(f"Car {car_type} could not be found!")
        car = cars[-1]
        if driver.car:
            old_car = driver.car
            driver.car = car
            old_car.is_taken = False
            car.is_taken = True
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        driver.car = car
        car.is_taken = True
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.get_race(race_name)
        driver = self.get_driver(driver_name)
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver.name in [x.name for x in race.drivers]:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.get_race(race_name)
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda x: -x.car.speed_limit)[:3]
        result = []
        for player in winners:
            player.number_of_wins += 1
            result.append(f"Driver {player.name} wins the {race_name} race with a speed of {player.car.speed_limit}.")

        return "\n".join(result)

    def get_race(self, race_name):
        result = next(filter(lambda x: x.name == race_name, self.races), None)
        if result:
            return result
        raise Exception(f"Race {race_name} could not be found!")

    def get_driver(self, driver_name):
        result = next(filter(lambda x: x.name == driver_name, self.drivers), None)
        if result:
            return result
        raise Exception(f"Driver {driver_name} could not be found!")
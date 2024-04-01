from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        self.astronaut_repository.add(self.ASTRONAUT_TYPES[astronaut_type](name))
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(amount=10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable_astronauts = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)[:5]
        counter = 0
        for astronaut in sorted_astronauts:
            if not planet.items:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. {counter} astronauts participated in collecting items."
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            counter += 1

        self.failed_missions += 1
        return f"Mission is not completed."

    def report(self):
        info = [f"{self.successful_missions} successful missions!",
                f"{self.failed_missions} missions were not completed!",
                "Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            items = ", ".join(astronaut.backpack) if astronaut.backpack else "none"
            info.append(f"Name: {astronaut.name}\n"
                        f"Oxygen: {astronaut.oxygen}\n"
                        f"Backpack items: {items}")

        return "\n".join(info)




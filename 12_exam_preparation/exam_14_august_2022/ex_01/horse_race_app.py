from typing import List
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def get_horse(self, horse_type):
        result = next(filter(lambda x: (type(x).__name__ == horse_type and not x.is_taken),
                             reversed(self.horses)), None)

        if result:
            return result
        raise Exception(f"Horse breed {horse_type} could not be found!")

    def get_race(self, race_type):
        result = next((r for r in self.horse_races if r.race_type == race_type), None)
        if result:
            return result
        raise Exception(f"Race {race_type} could not be found!")

    def get_jockey(self, jockey_name):
        result = next((j for j in self.jockeys if j.name == jockey_name), None)
        if result:
            return result
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSE_TYPES:
            self.horses.append(self.HORSE_TYPES[horse_type](horse_name, horse_speed))
            return f"{horse_type} horse {horse_name} is added."

        return

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        self.jockeys.append(Jockey(jockey_name, age))
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")
        self.horse_races.append(HorseRace(race_type))
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        horse = self.get_horse(horse_type)
        jockey = self.get_jockey(jockey_name)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.get_race(race_type)
        jockey = self.get_jockey(jockey_name)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.get_race(race_type)

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda j: -j.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
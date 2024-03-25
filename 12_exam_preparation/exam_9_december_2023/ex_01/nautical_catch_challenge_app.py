from ex_01.divers.base_diver import BaseDiver
from ex_01.divers.free_diver import FreeDiver
from ex_01.divers.scuba_diver import ScubaDiver
from ex_01.fish.base_fish import BaseFish
from ex_01.fish.deep_sea_fish import DeepSeaFish
from ex_01.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver,
                   "ScubaDiver": ScubaDiver
                   }
    FISH_TYPES = {"PredatoryFish": PredatoryFish,
                  "DeepSeaFish": DeepSeaFish

                  }

    def __init__(self):
        self.divers = []
        self.fish_list = []

    @staticmethod
    def check_for_health_issue(diver):
        if diver.oxygen_level == 0:
            diver.update_health_status()

    @staticmethod
    def invoke_hit_method(diver: BaseDiver, fish: BaseFish):
        diver.hit(fish)
        return f"{diver.name} hits a {fish.points}pt. {fish.name}."

    @staticmethod
    def invoke_miss_method(diver: BaseDiver, fish: BaseFish):
        diver.miss(fish.time_to_catch)
        return f"{diver.name} missed a good {fish.name}."

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = self.get_diver(diver_name)
        if diver:
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self.get_fish(fish_name)
        if fish:
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        result = ''
        diver = self.get_diver(diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.get_fish(fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            result = self.invoke_miss_method(diver, fish)
            self.check_for_health_issue(diver)
            return result

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                result = self.invoke_hit_method(diver, fish)
                self.check_for_health_issue(diver)
                return result

            result = self.invoke_miss_method(diver, fish)
            self.check_for_health_issue(diver)
            return result
        else:
            result = self.invoke_hit_method(diver, fish)
            self.check_for_health_issue(diver)
            return result

    def health_recovery(self):
        count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.update_health_status()
                diver.renew_oxy()
                count += 1
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_diver(diver_name)
        result = [f"**{diver_name} Catch Report**"]
        [result.append(fish.fish_details()) for fish in diver.catch]
        return "\n".join(result)

    def competition_statistics(self):
        divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = ["**Nautical Catch Challenge Statistics**"]
        [result.append(str(diver)) for diver in sorted_divers]

        return "\n".join(result)

    def get_fish(self, fish_name):
        return next((f for f in self.fish_list if f.name == fish_name), None)

    def get_diver(self, diver_name):
        return next((d for d in self.divers if d.name == diver_name), None)

from exam_01_december_2023.ex_01.peaks.base_peak import BasePeak


class SummitPeak (BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        if self.elevation > 2_500:
            return "Extreme"

        elif 1_500 <= self.elevation <= 2_500:
            return "Advanced"

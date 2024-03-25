from exam_01_december_2023.ex_01.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if self.elevation > 3_000:
            return "Extreme"

        elif 2_000 <= self.elevation <= 3_000:
            return "Advanced"

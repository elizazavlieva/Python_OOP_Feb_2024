from exam_01_december_2023.ex_01.climbers.base_climber import BaseClimber
from exam_01_december_2023.ex_01.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    STRENGTH = 150

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        multipy = 1.3 if peak.difficulty_level == "Advanced" else 2.5
        self.strength -= 30 * multipy
        self.conquered_peaks.append(peak.name)

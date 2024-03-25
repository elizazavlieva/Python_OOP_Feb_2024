from exam_01_december_2023.ex_01.climbers.base_climber import BaseClimber
from exam_01_december_2023.ex_01.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH = 200

    def __init__(self, name):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        multiply = 2.0 if peak.difficulty_level == "Extreme" else 1.5
        self.strength -= 20 * multiply
        self.conquered_peaks.append(peak.name)

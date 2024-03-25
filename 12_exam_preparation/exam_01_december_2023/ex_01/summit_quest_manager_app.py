from typing import List

from exam_01_december_2023.ex_01.climbers.arctic_climber import ArcticClimber
from exam_01_december_2023.ex_01.climbers.summit_climber import SummitClimber
from exam_01_december_2023.ex_01.peaks.arctic_peak import ArcticPeak
from exam_01_december_2023.ex_01.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber,
                     "SummitClimber": SummitClimber
    }
    PEAK_TYPES = {"ArcticPeak": ArcticPeak,
                  "SummitPeak": SummitPeak

    }

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        if self.get_climber(climber_name):
            return f"{climber_name} has been already registered."

        self.climbers.append(self.CLIMBER_TYPES[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.PEAK_TYPES[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self.get_climber(climber_name)
        peak = self.get_peak(peak_name)
        missing_gear = set(peak.get_recommended_gear()) - set(gear)
        if missing_gear:
            climber.is_prepared = False
            return f"{climber_name} is not prepared to climb {peak_name}. " \
                   f"Missing gear: {', '.join(sorted(missing_gear))}."

        return f"{climber_name} is prepared to climb {peak_name}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.get_climber(climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self.get_peak(peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

    def get_statistics(self):
        climbers = [c for c in self.climbers if c.conquered_peaks]
        sorted_climbers = sorted(climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        result = [f"Total climbed peaks: {len(self.peaks)}", "**Climber's statistics:**"]
        [result.append(str(climber)) for climber in sorted_climbers]

        return "\n".join(result)

    def get_peak(self, peak_name):
        return next((p for p in self.peaks if p.name == peak_name), None)

    def get_climber(self, climber_name):
        return next((c for c in self.climbers if c.name == climber_name), None)
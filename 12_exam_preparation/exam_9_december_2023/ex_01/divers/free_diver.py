from ex_01.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXY_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.INITIAL_OXY_LEVEL)

    def miss(self, time_to_catch: int):
        used_oxy = round(time_to_catch * 0.60)
        if self.oxygen_level >= used_oxy:
            self.oxygen_level -= used_oxy
        else:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXY_LEVEL

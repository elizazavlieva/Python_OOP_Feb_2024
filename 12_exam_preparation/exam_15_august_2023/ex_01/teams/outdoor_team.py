from ex_01.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    BUDGET = 1_000.0
    ADVANTAGE_POINTS = 115

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS
        self.wins += 1

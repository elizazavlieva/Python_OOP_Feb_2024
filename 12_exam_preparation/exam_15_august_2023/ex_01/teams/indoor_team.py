from ex_01.teams.base_team import BaseTeam


class IndoorTeam (BaseTeam):
    BUDGET = 500.0
    ADVANTAGE_POINTS = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.BUDGET)

    def win(self):
        self.advantage += self.ADVANTAGE_POINTS
        self.wins += 1

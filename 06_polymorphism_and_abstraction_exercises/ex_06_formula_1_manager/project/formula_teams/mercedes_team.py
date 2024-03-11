from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    sponsors = {"Petronas": {1: 1000000, 3: 500000}, "TeamViewer": {5: 100000, 7: 50000}}
    expenses = 200000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for positions in MercedesTeam.sponsors.values():
            for pos, money in positions.items():
                if race_pos <= pos:
                    revenue += positions[pos]
                    break
        revenue -= MercedesTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    sponsors = {"Oracle": {1: 1500000, 2: 800000}, "Honda": {8: 20000, 10: 10000}}
    expenses = 250000

    def __init__(self, budget):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        for positions in RedBullTeam.sponsors.values():
            for pos, money in positions.items():
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        revenue -= RedBullTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
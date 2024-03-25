from ex_01.equipment.elbow_pad import  ElbowPad
from ex_01.equipment.knee_pad import KneePad
from ex_01.teams.indoor_team import IndoorTeam
from ex_01.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    TEAM_TYPES = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment = [e for e in self.equipment if type(e).__name__ == equipment_type][-1]
        team = self.get_team(team_name)

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self,team_name: str):
        team = self.get_team(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins != 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count_of_change_equipment = len([equip.increase_price() for equip in self.equipment
                                         if type(equip).__name__ == equipment_type ])
        return f"Successfully changed {count_of_change_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self.get_team(team_name1)
        team2 = self.get_team(team_name2)

        if type(team1).__name__ != type(team2).__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        if team1.get_total_points() == team2.get_total_points():
            return "No winner in this game."
        winner = team1 if team1.get_total_points() > team2.get_total_points() else team2
        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"Tournament: {self.name}", f"Number of Teams: {len(self.teams)}","Teams:"]
        [result.append(team.get_statistics()) for team in sorted_teams]
        return "\n".join(result)


    def get_team(self, team_name):
        return next((t for t in self.teams if t.name == team_name), None)

    def get_equipment(self, equipment_type):
        return next((e for e in self.equipment if type(e).__name__ == equipment_type), None)
from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    @staticmethod
    def reduce_stamina_in_duel(attacked, attacker):
        result = attacked.stamina - attacker.stamina / 2
        attacked.stamina = 0 if result < 0 else result

    @staticmethod
    def winner(player):
        return f"Winner: {player.name}"

    def add_player(self, *players: Player):
        added_players = []
        for player in players:
            if player.name not in [x.name for x in self.players]:
                self.players.append(player)
                added_players.append(player)

        return f"Successfully added: {', '.join([x.name for x in added_players])}"

    def add_supply(self, *supplies: Supply):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((x for x in self.players if x.name == player_name), None)
        if not player:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type not in Supply.SUPPLY_TYPES:
            return

        for i in range(len(self.supplies) - 1, -1, -1):
            if type(self.supplies[i]).__name__ == sustenance_type:
                player.increase_stamina(self.supplies[i])
                result = self.supplies.pop(i)
                return f"{player_name} sustained successfully with {result.name}."

        if sustenance_type == "Food":
            raise Exception("There are no food supplies left!")
        elif sustenance_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def start_duel(self, attacked, attacker):
        self.reduce_stamina_in_duel(attacked, attacker)
        if attacked.check_player_stamina():
            return self.winner(attacker)

        self.reduce_stamina_in_duel(attacker, attacked)
        if attacker.check_player_stamina():
            return self.winner(attacked)

        winner = attacker if attacker.stamina > attacked.stamina else attacked
        return self.winner(winner)

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(filter(lambda x: x.name == first_player_name, self.players))
        player2 = next(filter(lambda x: x.name == second_player_name, self.players))

        if player1.check_player_stamina() and player2.check_player_stamina():
            return f"Player {player1.name} does not have enough stamina.\n" \
                   f"Player {player2.name} does not have enough stamina."
        if player1.check_player_stamina():
            return f"Player {player1.name} does not have enough stamina."
        elif player2.check_player_stamina():
            return f"Player {player2.name} does not have enough stamina."

        if player1.stamina < player2.stamina:
            return self.start_duel(player2, player1)
        else:
            return self.start_duel(player1, player2)

    def next_day(self):
        for player in self.players:
            player.reduce_stamina()

            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        information = [str(x) for x in self.players]
        [information.append(x.details()) for x in self.supplies]

        return "\n".join(information)


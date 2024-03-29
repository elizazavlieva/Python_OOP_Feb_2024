from guild_system.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == "Unaffiliated":
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        remove_player = [player_ for player_ in self.players if player_.name == player_name]

        if remove_player:
            remove_player[0].guild = "Unaffiliated"
            self.players.remove(remove_player[0])
            return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players = "\n".join([cur_player.player_info() for cur_player in self.players])
        return f"Guild: {self.name}\n{players}"



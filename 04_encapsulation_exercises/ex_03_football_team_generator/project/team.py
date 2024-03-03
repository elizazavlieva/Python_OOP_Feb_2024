from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        for pl in self.__players:
            if pl == player:
                return f"Player {pl.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for pl in self.__players:
            if pl.name == player_name:
                self.__players.remove(pl)
                return pl

        return f"Player {player_name} not found"


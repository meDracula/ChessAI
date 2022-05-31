from kuhn.table import Table
from kuhn.player import Player

class Kuhn:
    deck_value = {"J": 1, "Q": 2, "K": 3}

    def new_match(self, *names):
        self.table = Table([Player(name) for name in names])

    def pre_showdown(self):
        self.table.pre_showdown()
        return {player.name: player.hand for player in self.table.players}

    def showdown(self):
        player = {player.name: self.deck_value[player.hand] for player in self.table.players}
        return max(player, key=player.get)

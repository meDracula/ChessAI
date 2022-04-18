from table import Table
from player import Player
from scorer import Scorer


class Poker:
    def __init__(self):
        self.table = None


    def new_game(self, *names):
        players = [Player(name) for name in names]
        self.table = Table(*players)

        self.table.preflop()
        return {player.name: player.hand for player in self.table.players}


    def flop(self, *drop_players):
        for player_name in drop_players:
            self.table.player_out(player_name)

        if len(self.table.players) == 1:
            return self.winner()

        self.table.flop()
        return {'community cards': str(self.table)}


    def turn(self, *drop_players):
        for player_name in drop_players:
            self.table.player_out(player_name)

        if len(self.table.players) == 1:
            return self.winner()

        self.table.turn()
        return {'community cards': str(self.table)}


    def river(self, *drop_players):
        for player_name in drop_players:
            self.table.player_out(player_name)

        if len(self.table.players) == 1:
            return self.winner()

        self.table.river()
        return {'community cards': str(self.table)}


    def winner(self):
        player = Scorer(self.table).get_winner()
        return {'winner': (player.name, player.hand)}

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


    def folds(self, *players):
        for player_name in players:
            self.table.player_fold(player_name)


    def __iter__(self):
        self.rounds = 0
        return self


    def __next__(self):
        self.rounds += 1
        return self.next_round(self.rounds)


    def next_round(self, rounds):
        match rounds:
            case 1:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.flop()
                return {'community cards': str(self.table)}
            case 2:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.turn()
                return {'community cards': str(self.table)}
            case 3:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.river()
                return {'community cards': str(self.table)}
            case 4:
                return self.winner()
        raise StopIteration()


    def winner(self):
        player = Scorer(self.table).get_winner()
        return {'winner': (player.name, player.hand)}


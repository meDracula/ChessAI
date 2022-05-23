from kuhn.dealer import Dealer

class Table:
    def __init__(self, players: dict):
        self.players = players
        self.dealer = Dealer()

    def pre_showdown(self):
        for player in self.players:
            player.hand = self.dealer.deal()

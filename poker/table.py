from dealer import Dealer


class Table:
    def __init__(self, *players):
        self.players = list(players)
        self.dealer = Dealer()
        self.community_cards = []

    def preflop(self):
        for player in self.players:
            player.cards = self.dealer.deal(2)

    def flop(self):
        self.community_cards = self.dealer.deal(3)

    def turn(self):
        self.community_cards += self.dealer.deal(1)

    def river(self):
        self.community_cards += self.dealer.deal(1)

    def player_fold(self, name):
        player = next(player for player in self.players if player.name == name)
        self.players.remove(player)
        del player.hand

    def __repr__(self):
        return f"{self.community_cards}"

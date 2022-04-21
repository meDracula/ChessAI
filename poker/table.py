from .dealer import Dealer


class Table:
    def __init__(self, *players):
        self.player_table = list(players)
        self.players = []
        self.dealer = Dealer()
        self.community_cards = []

    def preflop(self):
        for player in self.player_table:
            player.cards = self.dealer.deal(2)
            self.players.append(player)

    def flop(self):
        self.community_cards = self.dealer.deal(3)

    def turn(self):
        self.community_cards += self.dealer.deal(1)

    def river(self):
        self.community_cards += self.dealer.deal(1)

    def player_fold(self, name):
        player = next((player for player in self.players if player.name == name), None)
        if player is not None:
            self.players.remove(player)
            del player.hand

    def player_leave(self, name):
        for player in (player for player in self.player_table if player.name == name):
            self.player_table.remove(player)
            del player

    def __repr__(self):
        return f"{self.community_cards}"

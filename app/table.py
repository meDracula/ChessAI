from app.dealer import Dealer



class Table():
    def __init__(self, *players):
        self.players = players
        self.dealer = Dealer()
        self.community_cards = []


    def preflop(self):
        for player in self.players:
            player.cards.append(self.dealer.deal(2))

    def flop(self):
        self.community_cards.append(self.dealer.deal(3))

    def turn(self):
        self.community_cards.append(self.dealer.deal(1))

    def river(self):
        self.community_cards.append(self.dealer.deal(1))








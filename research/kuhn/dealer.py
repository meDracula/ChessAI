from random import shuffle

class Dealer:
    def __init__(self):
        self.deck = Dealer.init_deck()

    def deal(self):
        return self.deck.pop(0)

    @staticmethod
    def init_deck():
        deck = ["J", "Q", "K"]
        shuffle(deck)
        return deck

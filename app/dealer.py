from random import shuffle


class Dealer:
    def __init__(self):
        self.deck = self.init_deck()

    def deal(self, n_cards):
        return [self.deck.pop(0) for _ in range(n_cards)]

    def reset_deck(self):
        self.deck = self.init_deck()

    @classmethod
    def init_deck(cls):
        suits = ["D", "H", "S", "C"] # D: DIAMOND, H: HEART, S: SPADE, C: CLUB
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "D", "K", "A"]
        deck = [rank+suit for rank in ranks for suit in suits]
        shuffle(deck)
        return deck

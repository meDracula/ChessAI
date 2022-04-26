from poker.deck import Deck


class Dealer:
    def __init__(self):
        self.deck = Deck.init_deck()

    def deal(self, n_cards):
        return [self.deck.pop(0) for _ in range(n_cards)]

    def reset_deck(self):
        self.deck = self.init_deck()

    def cards_left(self):
        return len(self.deck)

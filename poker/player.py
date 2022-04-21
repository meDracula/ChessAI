from deck import Deck

class Player:
    def __init__(self, name=None):
        self.name = name
        self.cards = []

    @property
    def hand(self):
        return self.cards

    @hand.setter
    def hand(self, new_cards):
        if not(isinstance(new_cards, list) and len(new_cards) == 2):
            print("Invalide deck format")
            return None

        og_deck = Deck.init_deck()
        if all(card in og_deck for card in new_cards):
            self.cards = new_cards
        else:
            print("Invalide assets format")
            return None

    @hand.deleter
    def hand(self):
        self.cards = []

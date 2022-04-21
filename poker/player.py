from .deck import Deck, Template_Deck


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

        if all(card in Template_Deck for card in new_cards):
            self.cards = new_cards
        else:
            print("Invalide cards format")

    @hand.deleter
    def hand(self):
        self.cards = []


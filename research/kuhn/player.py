class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    @property
    def hand(self):
        return self.cards

    @hand.setter
    def hand(self, new_cards):
        self.cards = new_cards

    @hand.deleter
    def hand(self):
        self.cards = []

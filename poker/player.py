class Player:
    def __init__(self, name=None):
        self.name = name
        self.cards = []

    @property
    def hand(self):
        return self.cards

    @hand.setter
    def hand(self, new_cards):
        # This code card logic can be altered when decide deck structure exist
        is_hand = isinstance(new_cards, list) and len(new_cards) == 2
        is_cards = all(isinstance(card, str) and len(card) == 2 for card in new_cards)
        if is_hand and is_cards:
            self.cards = new_cards
        else:
            print("Invalide cards formality")

    @hand.deleter
    def hand(self):
        self.cards = []


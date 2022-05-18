class Callie:
    def __init__(self):
        self.hand = None
        self.community_cards = None
        self.players_fold = None

    def get_hand(self, hand):
        self.hand = hand

    def obeservation(self, community_cards, players_fold):
        self.community_cards = community_cards
        self.players_fold = players_fold

    def action(self):
        return 'call'

    def clear(self):
        self.hand = None
        self.community_cards = None
        self.players_fold = None

from callie import Callie

class MiddleMan:
    def __init__(self, name):
        self.name = name
        self.bot = Callie()

    def new_match(self):
        self.bot.clear()

    def get_hand(self, hand):
        self.bot.get_hand(hand)

    def update_enviroment(self, community_cards, players_fold):
        self.bot.obeservation(community_cards, players_fold)

    def action(self):
        # Acceptable actions 'call' or 'fold'
        return self.bot.action()


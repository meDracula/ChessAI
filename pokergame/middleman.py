from pokergame.callie import Callie
from neural_network.model import PokerAI

class MiddleMan:
    def __init__(self, name):
        self.name = name
        self.bot = PokerAI.load_model()

    def new_match(self):
        self.bot.clear()

    def get_hand(self, hand):
        self.bot.get_hand(hand)

    def update_enviroment(self, community_cards, players_fold):
        self.bot.observation(community_cards, players_fold)

    def action(self):
        # Acceptable actions 'call' or 'fold'
        return self.bot.action()


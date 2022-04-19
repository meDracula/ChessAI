from treys import Evaluator
from treys import Card


class Scorer:
    def __init__(self, table):
        self.table = table
        self.evaluator = Evaluator()

    # convert to trey library Card class
    def convert_cards(self, cards):
        return [Card.new(card) for card in cards]

    def get_winner(self):
        player_scores = {}
        community_cards = self.convert_cards(self.table.community_cards)
        for player in self.table.players:
            player_scores[player] = self.evaluator.evaluate(community_cards, self.convert_cards(player.cards))

        return min(player_scores, key=player_scores.get)  # return player with best score (lower scores are better)

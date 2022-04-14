from treys import Evaluator
from treys import Card


class Scorer:
    def __init__(self, table):
        self.table = table
        self.evaluator = Evaluator()

    # convert to trey library Card class
    def convert_cards(self, cards):
        trey_cards = []
        for card in cards:
            trey_cards.append(Card.new(card))
        return trey_cards

    def get_winner(self):
        player_scores = {}
        for player in self.table.players:
            player_score = self.evaluator.evaluate(self.convert_cards(self.table.community_cards), self.convert_cards(player.cards))
            player_scores[player] = player_score

        return min(player_scores, key=player_scores.get)  # return player with best score (lower scores are better)

from scorer import *
from table import *


class Player:
    def __init__(self):
        self.cards = []


class Scorer:
    def __init__(self, tabbel):
        self.table = tabbel
        self.evaluator = Evaluator()

    # convert to trey library Card class
    def convert_cards(self, cards):
        trey_cards = []
        for card in cards:
            if card.startswith('10'):
                trey_cards.append(Card.new(card.replace('10', 'T')))
            else:
                trey_cards.append(Card.new(card))
        return trey_cards

    def get_winner(self):
        player_scores = {}
        for player in self.table.players:
            player_score = self.evaluator.evaluate(self.convert_cards(self.table.community_cards), self.convert_cards(player.cards))
            player_scores[player] = player_score

        return min(player_scores, key=player_scores.get)  # return player with best score (lower scores are better)


if __name__ == '__main__':
    p1, p2 = Player(), Player()
    table = Table(p1, p2)
    table.preflop()
    table.flop()
    print(p1.cards, p2.cards)
    score = Scorer(table)
    print(score.get_winner().cards)

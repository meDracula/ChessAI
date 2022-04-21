from treys import Evaluator
from treys import Card


# convert to trey library Card class
def convert_cards(cards):
    return [Card.new(card) for card in cards]


def winner_is(table):
    evaluator = Evaluator()
    player_scores = {}

    community_cards = convert_cards(table.community_cards)
    for player in table.players:
        player_scores[player] = evaluator.evaluate(community_cards, convert_cards(player.cards))

    return min(player_scores, key=player_scores.get)  # return player with best score (lower scores are better)


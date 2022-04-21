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

def determine_winner(community_cards, *players):
    def winner_is(p1, p2, community_cards):
        counter = lambda cards: {card: cards.count(card) for card in cards if cards.count(card) > 1 }

    for _ in range(len(players)-1):
        compare, players = players[:2], players[2:]
        winner = winner_is(compare[0], compare[1], community_cards)
        players.append(winner)


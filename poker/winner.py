from treys import Evaluator
from treys import Card


# convert to trey library Card class
def convert_cards(cards):
    return [Card.new(card) for card in cards]


def winner_is(players: list, community_cards: list):
    evaluator = Evaluator()
    player_scores = {}

    community_cards = convert_cards(community_cards)
    for player in players:
        player_scores[player] = evaluator.evaluate(community_cards, convert_cards(player.cards))

    return min(player_scores, key=player_scores.get)  # return player with best score (lower scores are better)

def hand_summary(player, community_cards: list):
    evaluator = Evaluator()
    community_treys = convert_cards(community_cards)
    player_trey = convert_cards(player.hand)

    player_map_prob = []
    for i in range(3, 6):
        rank = evaluator.evaluate(player_trey, community_treys[:i])
        percentage = 1 - evaluator.get_five_card_rank_percentage(rank)
        player_map_prob.append(percentage)
    return player_map_prob


import json
from collections import Counter
from pokergame import settings

def save_winner(winner):
    with open(settings.LEADERBOARD_SAVE, 'a', encoding='utf-8') as leaderboard:
        leaderboard.write(json.dumps(winner))
        leaderboard.write('\n')


def show_leaderboard():
    winning_player = []
    winning_hand = []

    with open(settings.LEADERBOARD_SAVE, 'r', encoding='utf-8') as leaderboard_r:
        for lines in leaderboard_r:
            res = json.loads(lines)
            winning_player.append(res['winner'][0])
            winning_hand.append(f"{res['winner'][1][0]} {res['winner'][1][1]}")
        top_5_players = (Counter(winning_player).most_common(5))
        top_5_hands = (Counter(winning_hand).most_common(5))

        return top_5_players, top_5_hands

import json
from collections import Counter

def save_winner(winner):

    with open('leaderboard_save', 'a', encoding='utf-8') as leaderboard:
        leaderboard.write(json.dumps(winner))
        leaderboard.write('\n')


def show_leaderboard():
    top_list = []
    with open('leaderboard_save', 'r', encoding='utf-8') as leaderboard_r:
        for lines in leaderboard_r:
            res = json.loads(lines)
            top_list.append(res['winner'][0])
            print(res['winner'][0])
            print(top_list)
            print(Counter(top_list))




def main():
    save_winner({'winner': ('marco', ['ac', 'hc'])})
    show_leaderboard()


if __name__ == '__main__':
    main()
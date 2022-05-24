def card_compute(card):
    suits = {"h": 0, "d": 1,"c": 2, "s": 3}
    ranks = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}
    return ranks[card[0]] + suits[card[1]] * 13

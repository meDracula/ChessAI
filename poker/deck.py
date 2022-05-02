from random import shuffle


class Deck:
    suits = ["d", "h", "s", "c"] # d: DIAMOND, h: HEART, s: SPADE, c: CLUB
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] # T: 10
    royalface = "TJQKA"

    @classmethod
    def init_deck(cls):
        deck = [rank+suit for rank in cls.ranks for suit in cls.suits]
        shuffle(deck)
        return deck


Template_Deck = tuple(Deck.init_deck())

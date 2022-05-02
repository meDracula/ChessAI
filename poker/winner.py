from poker.deck import Deck


class Ranking:
    def __init__(self, cards):
        self.cards = cards
        self.counter = lambda cards: {card: cards.count(card) for card in cards if cards.count(card) > 1 }
        self.suits = [card[1] for card in cards]
        self.ranks = [card[0] for card in cards]
        self.deck_value = {key: val+2 for val, key in enumerate(Deck.ranks)}
        self.ranks_sort = sorted([self.deck_value[card[0]] for card in cards])


    def royal_flush(self):
        if sum(rank in Deck.royalface for rank in self.ranks) >= 5:
            royal = [card for card in self.cards if card[0] in Deck.royalface]
            if all(card[1] == royal[0][1] for card in royal):
                return True
        return False

    def straight_flush(self):
        for i in range(3):
           straight = self.ranks[i:5+i] == list(range(min(self.ranks[i:]), max(self.ranks[i:5+i])+1))
           flush = any(filter(lambda suit: suit>4, self.counter(self.suits[i:5+1]).values()))
           if straight and flush:
               return True
        return False

    def four_of_kind(self):
        return True if any(filter(lambda rank: rank == 4, self.counter(self.ranks).values())) else False

    def full_house(self):
        tripplet = any(filter(lambda rank: rank==3, self.counter(self.ranks).values()))
        return True if tipplet and any(filter(lambda rank: rank==2, self.counter(self.ranks).values())) else False

    def flush(self):
        return True if any(filter(lambda suit: suit>4, self.counter(self.suits).values())) else False

    def straight(self):
        return True if any(rank_card[i:5+i] == list(range(rank_card[i], rank_card[5+i]+1)) for i in range(3)) else False

    def three_of_kind(self):
        return True if any(filter(lambda rank: rank==3, self.counter(self.ranks).values())) else False

    def two_pair(self):
        return True if len(list(filter(lambda rank: rank==2, self.counter(self.ranks).values()))) else False

    def one_pair(self):
        return True if any(filter(lambda rank: rank==2, self.counter(self.ranks).values())) else False

    def result(self):
        rankings = [self.royal_flush, self.straight_flush, self.four_of_kind, self.full_house,
                    self.flush, self.straight, self.three_of_kind, self.two_pair, self.one_pair]
        for index, ranking in enumerate(rankings):
            if ranking():
                return len(rankings)-index
        return 0


def high_card(hand_1, hand_2):
    deck_value = {key: val+2 for val, key in enumerate(Deck.ranks)}
    p1_rank = [deck_value[card[0]] for card in hand_1]
    p2_rank = [deck_value[card[0]] for card in hand_2]
    if max(p1_rank) > max(p2_rank):
        return p1
    elif max(p1_rank) == max(p2_rank):
        return p1 if min(p1_rank) > min(p2_rank) else p2
    else:
        return p2


def winner_is(community_cards, *players):
    def winner_is(p1, p2, community_cards):
        p1_rank = Ranking(p1.hand+community_cards).result()
        p2_rank = Ranking(p2.hand+community_cards).result()
        if p1_rank == 0 and p2_rank == 0:
            return high_card(p1.hand, p2.hand)
        return max(p1_rank, p2_rank)

    for _ in range(len(players)-1):
        compare, players = players[:2], players[2:]
        winner = winner_is(compare[0], compare[1], community_cards)
        players.append(winner)


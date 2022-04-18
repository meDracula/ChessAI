def determine_winner(community_cards, *players):
    def winner_is(p1, p2, community_cards):
        counter = lambda cards: {card: cards.count(card) for card in cards if cards.count(card) > 1 }

    for _ in range(len(players)-1):
        compare, players = players[:2], players[2:]
        winner = winner_is(compare[0], compare[1], community_cards)
        players.append(winner)


if __name__ == '__main__':
    from table import Table
    from player import Player
    p1, p2 = Player(), Player()
    table = Table(p1, p2)
    table.preflop()
    print("Table: ", "player 1:", p1.hand, "player 2:", p2.hand)
    print("Flop")
    table.flop()
    print("Table: ", table, "player 1:", p1.hand, "player 2:", p2.hand)
    print("Turn")
    table.turn()
    print("Table: ", table, "player 1:", p1.hand, "player 2:", p2.hand)
    print("River")
    table.river()
    print("Table: ", table, "player 1:", p1.hand, "player 2:", p2.hand)

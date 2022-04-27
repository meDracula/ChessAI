import unittest

from poker import Poker


class TestPoker(unittest.TestCase):
    # test where no active actions are taken by the players
    def test_poker_game(self):
        poker_game = Poker()
        poker_game.new_game("Olle", "Kalle")
        poker_game.new_match()
        [poker_game.next_round(i) for i in range(1, 5)]

        print("community cards: ", poker_game.table)
        print(poker_game.table.players)
        print(poker_game.winner())

    def test_poker_game_fold(self):
        poker_game = Poker()
        poker_game.new_game("Olle", "Maria", "Kalle", "Anna")
        poker_game.new_match()

        for i in range(1, 5):
            if i == 4:
                poker_game.table.player_fold("Kalle")   # kalle leaves the current game here in the last round
            poker_game.next_round(i)

        print("\nCommunity cards: ", poker_game.table)
        print(poker_game.table.players)
        print(poker_game.winner())


if __name__ == '__main__':
    unittest.main()

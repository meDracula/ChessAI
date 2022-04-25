import unittest

from poker.player import Player
from poker.table import Table


class Testplayer(unittest.TestCase):

    def test_player_hand(self):
        player1, player2 = Player("Olle"), Player("Kalle")
        print(player1, player2)

        table = Table(player1, player2)
        print(f"The Table: {table}")

        table.preflop()
        table.flop()

        print(player1, player2)
        print(f"The Table: {table}")

        del player1.hand
        print(player1, player2)


if __name__ == '__main__':
    unittest.main()

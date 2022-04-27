import unittest

from poker.player import Player
from poker.table import Table


class Testplayer(unittest.TestCase):

    def test_player_hand(self):
        player1, player2 = Player("Olle"), Player("Kalle")
        print(f"First_print: {player1, player2}")
        table = Table(players={"1": player1, "2": player2})
        print(f"The Table: {table}\n")

        table.preflop()
        table.flop()
        print(f"secound_print: {player1, player2}")
        print(f"The Table: {table}\n")

        del player1.hand
        print(player1, player2)


if __name__ == '__main__':
    unittest.main()

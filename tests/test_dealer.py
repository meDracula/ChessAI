import unittest

from poker.dealer import Dealer


class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()

    def test_reset_deck(self):
        print(self.dealer.deck)
        self.dealer.reset_deck()
        print(self.dealer.deck)

    def test_cards_left(self):
        self.assertTrue(self.dealer.cards_left() == 52)


if __name__ == '__main__':
    unittest.main()

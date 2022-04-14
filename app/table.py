from app.dealer import Dealer


class PokerTable():
    def __init__(self):
        #self.player = Player()
        self.dealer = Dealer()
        self.board = []
        self.pot = 0


    def deal_cards(self):
        for player in self.player:
            player.cards.append(self.dealer.deal(2))

    def the_flop(self):
        self.board.append(self.dealer.deal(3))

    def turn_river(self):
        self.board.append(self.dealer.deal(1))


    def bets(self):
        if self.player._raise:
            self.pot += self.player._raise


    def player_turn(self):
        for player in self.player:
            match player:
                case player.fold:
                    pass
                case player._raise:
                    self.bets()
                case  player.check:
                    pass







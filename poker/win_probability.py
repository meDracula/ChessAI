

class WinProbability:
    def __init(self, dealer, *players, scorer, table):
        self.dealer = dealer
        self.players = players
        self.scorer = scorer
        self.table = table
        self.player_scores = {}

    def cards_needed(self):
        new_score = 0
        for card in self.dealer.deck:
            self.scorer.convert_cards(card)
            new_score = self.scorer.evaluator.evaluate(self.scorer.convert_cards(card),
                                                       self.scorer.convert_cards(player.cards))
            for player in self.players:
                if new_score > self.player_scores:
                    return 1

    def odds_per_card(self):
        cards_in_deck = self.dealer.cards_left
        cards_needed = self.cards_needed
        per_card = cards_needed/cards_in_deck
        percentage = f"{per_card:.0%}"
        return percentage

    def leading_hand(self):

        for player in self.table.players:
            self.player_score = self.scorer.evaluator.evaluate(self.scorer.convert_cards(self.table.community_cards),
                                                          self.scorer.convert_cards(player.cards))
            self.player_scores[player] = self.player_score


w = WinProbability()
print(w.odds_per_card())

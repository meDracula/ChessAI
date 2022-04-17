
class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.chips = 0
        self.cards = []
        self.score = []
        self.fold = False
        self.ready = False
        self._raise = False
        self.win = False
        self.lose = False

    def __repr__(self):
        name = self.name
        return name

    def show_player_card(self):
        synonym_show_cards = ["show cards", "show my cards", "show hand", "my cards"]

        if synonym_show_cards:
            return f"This is your cards: {self.cards}"


    def player_choice(self, player):
        synonym_fold = ""
        synonym_raise = ""
        synonym_ready = ""

        if player in synonym_fold:
            player = "fold"
            return player

        elif player in synonym_raise:
            player = "raise"
            return player

        elif player in synonym_ready:
            player = "ready"
            return player

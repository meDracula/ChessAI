
class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.chips = 0
        self.card = []
        self.score = []
        self.fold = False
        self.ready = False
        self._raise = False
        self.win = False
        self.lose = False

    def __repr__(self):
        name = self.name
        return name

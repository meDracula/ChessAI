from poker.table import Table
from poker.player import Player
from poker.winner import winner_is


class Poker:
    def new_game(self, *names):
        """Start a new poker game, and no return.

            Every player name entered as a argument to parameter names will be create.
            The function will setup a table with all of the new players entered.

            :param names: Multiple arguments of str of names.
            :type names: tuple
            :type name: str
        """
        players = [Player(name) for name in names]
        self.table = Table(players)


    def new_match(self, player_leave=[], player_new=[]):
        """Start a new poker match, and returns a dictonary of all players cards.

            Function new_match will start a match of poker.
            This function requires that new_game function have been executed first.
            new_match allows players to leave or add new players to play.

            :param player_leave: list of player names that will leave the game.
            :param player_new: list of new names of players to create for the game.
            :type player_leave: list
            :type player_new: list
            :type name: str

            :return: A dictonary { player name: hand }, key player name, value player hand
        """
        if len(player_new) > 0:
            self.table.player_table += [Player(name) for name in player_new]

        if len(player_leave) > 0:
            for name in player_leave:
                self.table.player_leave(name)

        self.table.preflop()
        return {player.name: player.hand for player in self.table.players}


    def folds(self, *names):
        """The function will fold playing players from the match, return nothing.

            :param names: multiple arguments of player names.
            :type names: tuple
            :type name: str
        """
        for player_name in players:
            self.table.player_fold(player_name)


    def __iter__(self):
        self.rounds = 0
        return self


    def __next__(self):
        self.rounds += 1
        return self.next_round(self.rounds)


    def next_round(self, rounds):
        match rounds:
            case 1:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.flop()
                return {'community cards': str(self.table)}
            case 2:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.turn()
                return {'community cards': str(self.table)}
            case 3:
                if len(self.table.players) == 1:
                    return self.winner()
                self.table.river()
                return {'community cards': str(self.table)}
            case 4:
                return self.winner()
        raise StopIteration()


    def winner(self):
        """This function evaluates the winner of current playing players in a match, returns the winning player.

            :return: {'winner': (name, hand)} A dictionary with key winner and value tuple player name and hand
        """
        player = winner_is(self.table)
        return {'winner': (player.name, player.hand)}

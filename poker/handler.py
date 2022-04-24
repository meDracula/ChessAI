from poker.table import Table
from poker.player import Player
from poker.winner import winner_is


class Poker:
    def new_game(self, *names):
        """
            Start a new poker game.

            :param names: Write name, name, ..., name for every player to create.
        """
        players = [Player(name) for name in names]
        self.table = Table(players)


    def new_match(self, player_leave=[], player_new=[]):
        """
            Start a new poker match.

            :param player_leave: A empty list where names of players are named that will leave the game.
            :param player_new: A empty list where new names of players that will be created are add to.

            :return: A dictonary { player name: hand }, key player name, value player hand
        """
        if len(player_new) > 0:
            self.table.player_table += [Player(name) for name in player_new]

        if len(player_leave) > 0:
            for name in player_leave:
                self.table.player_leave(name)

        self.table.preflop()
        return {player.name: player.hand for player in self.table.players}


    def folds(self, *players):
        """
            The function will fold mentioned active players in a match.

            :param players: Write name, name, ..., name of player names
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
        """
            This function evaluates the winner of current table left on the table.

            :return: {'winner': (name, hand)} A dictionary with key winner and value tuple player name and hand
        """
        player = winner_is(self.table)
        return {'winner': (player.name, player.hand)}


from poker.table import Table
from poker.player import Player
from poker.winner import winner_is, hand_summary


class Poker:
    def new_game(self, *names):
        """Start a new poker game, and no return.

            Every player name entered as a argument to parameter names will be create.
            The function will setup a table with all of the new players entered.

            :param names: Multiple arguments of str of names.
            :type names: *args
            :type name: str
        """
        self.table = Table({name: Player(name) for name in names})

    def new_match(self, player_leave=[], player_add=[]):
        """Start a new poker match, and returns a dictonary of all players cards.

            Function new_match will start a match of poker.
            This function requires that new_game function have been executed first.
            new_match allows players to leave or add new players to play.

            :param player_leave: list of player names that will leave the game.
            :param player_add: list of new names of players to create for the game.
            :type player_leave: list
            :type player_add: list
            :type name: str

            :return: A dictonary { player name: hand }, key player name, value player hand
        """
        self.table.clear()

        if len(player_add) > 0:
            for name in player_add:
                if name not in self.table.player_table:
                    self.table.player_table[name] = Player(name)
                else:
                    raise ValueError("Player name already taken!")

        if len(player_leave) > 0:
            if all(player in self.table.player_table for player in player_leave):
                self.table.player_leave(player_leave)
            else:
                raise ValueError("Player leave name is unknown!")

        self.table.preflop()
        return {player.name: player.hand for player in self.table.players}

    def folds(self, *names):
        """The function will fold playing players from the match, return nothing.

            :param names: multiple arguments of player names.
            :type names: tuple
            :type name: str
        """
        if set(names).issubset([player.name for player in self.table.players]):
            self.table.player_fold(names)
        else:
            raise ValueError("Player name is not playing a match!")

    def __iter__(self):
        self.rounds = 0
        return self

    def __next__(self):
        self.rounds += 1
        if len(self.table.players) > 1:
            return self.next_round(self.rounds)
        else:
            raise StopIteration()

    def next_round(self, rounds):
        match rounds:
            case 1:
                self.table.flop()
                return {'community cards': self.table.community_cards}
            case 2:
                self.table.turn()
                return {'community cards': self.table.community_cards}
            case 3:
                self.table.river()
                return {'community cards': self.table.community_cards}
        raise StopIteration()

    def winner(self):
        """This function evaluates the winner of current playing players in a match, returns the winning player.

            :return: {'winner': (name, hand)} A dictionary with key winner and value tuple player name and hand
        """
        if len(self.table.players) == 1:
            player = self.table.players[0]
        else:
            player = winner_is(self.table.players, self.table.community_cards)
        return {f'winner': (player.name, player.hand)}

    def exepected_outcome(self, player: str):
        """Exepcted outcome for a player to playout.
            This function evalutes how the game can play out and recommeded course of action for player.

            :param player: A players name for the function to create the exepcted outcome for.
            :type player: str

            :return: tuple of exepected choice [ call, fold ]
        """
        # Bad hand combinations
        player_obj = self.table.player_table[player]
        bad_hand_combo = ["2", "7"], ["2", "8"], ["3", "8"], ["2", "9"], ["2", "6"]  # All offsuit
        hand_rank = {player_obj.hand[0][0], player_obj.hand[1][0]}
        if player_obj.hand[0][1] != player_obj.hand[1][1] and any(hand_rank == set(combo) for combo in bad_hand_combo):
            #return [0, 1], [0, 1], [0, 1], [0, 1]  # Fold on pre flop
            return 0, 0, 0, 0

        # All players call outcome
        community_cards = self.table.dealer.deck[:5]
        winning_player = winner_is(self.table.players, community_cards)
        if winning_player.name == player:
            #return [1, 0], [1, 0], [1, 0], [1, 0]
            return 1, 1, 1, 1

        # Calculating when to fold
        deviation_fold = 0.2
        percentage_dist = hand_summary(player_obj, community_cards)
        if percentage_dist[1] < 0.1 and percentage_dist[0] + deviation_fold > percentage_dist[1]:
            #return [1, 0], [0, 1], [0, 1], [0, 1]  # Fold on flop
            return 1, 0, 0, 0

        elif percentage_dist[2] < 0.70:
            #return [1, 0], [1, 0], [0, 1], [0, 1]  # Fold on river
            return 1, 1, 0, 0

        else:
            #return [1, 0], [1, 0], [1, 0], [1, 0]  # Don't fold to good of a hand
            return 1, 1, 0, 0

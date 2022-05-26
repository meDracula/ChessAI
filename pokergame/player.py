import pygame
from pokergame import settings


class PlayerHandler:
    def __init__(self, players: dict, cardhandler):
        self.players = players
        self.cardhandler = cardhandler

        self.load_positions(players)

        self.folds = []
        self.player_round = {player: "wait" for player in players} # Acceptable values: wait, call or fold
        self.player_next = iter(self.player_round)
        self.current_player = next(self.player_next)
        self.previous_act = None
        self.next_round = False
        self.preflop = True

        self.call = None
        self.fold = None

        self.font_player_name = pygame.font.Font('freesansbold.ttf', 40)
        self.font_player_name.italic = True

    def load_positions(self, players):
        self.player_positions = {}
        for index, player in enumerate(players):
            if index == 0:
                pos_card = (250, 130)
                pos_call = (290, 240)
                pos_player = (310, 60)
            elif index == 1:
                pos_card = (250, 550)
                pos_call = (290, 510)
                pos_player = (310, 665)
            elif index == 2:
                pos_card = (500, 550)
                pos_call = (540, 510)
                pos_player = (560, 665)
            elif index == 3:
                pos_card = (500, 130)
                pos_call = (540, 240)
                pos_player = (560, 60)
            self.player_positions[player] = {'card': pos_card, 'call': pos_call, 'player': pos_player}
        self.offset_call_x = 110
        self.offset_card_x = 70

    def draw_players(self, game):
        for player in self.players:
            card_pos = self.player_positions[player]['card']
            for card in self.players[player]:
                card_pos = (card_pos[0] + self.offset_card_x, card_pos[1])
                self.cardhandler.draw_player_cards(game, card, card_pos)

            # Player name tag
            player_place_text = self.font_player_name.render(player, True, (0, 0, 255))
            game.screen.blit(player_place_text, self.player_positions[player]['player'])

        # Draw call and fold
        pos = self.player_positions[self.current_player]['call']
        self.call = pygame.draw.rect(game.screen, (0, 0, 0), (pos[0] - 10, pos[1] - 7, 100, 40), 2)
        call_text = game.font.render(settings.CALL_TEXT, True, (255, 255, 255))

        pos_fold_x = pos[0] + self.offset_call_x
        self.fold = pygame.draw.rect(game.screen, (0, 0, 0), (pos_fold_x - 10, pos[1] - 7, 100, 40), 2)
        fold_text = game.font.render(settings.FOLD_TEXT, True, (255, 255, 255))

        game.screen.blit(call_text, pos)
        game.screen.blit(fold_text, (pos[0] + self.offset_call_x, pos[1]))

    def next_player(self, action):
        self.player_round[self.current_player] = action
        self.previous_act = (self.current_player, action)

        if not all(act != "wait" for act in self.player_round.values()):
            self.current_player = next(self.player_next)
        else:
            # Next round / Reset Cycle
            for player in list(self.player_round.keys()):
                if self.player_round[player] == "fold":
                    self.player_round.pop(player)
                    self.folds.append(player)
                else:
                    self.player_round[player] = "wait"

            self.preflop = False
            self.player_next = iter(self.player_round)
            self.current_player = next(self.player_next)
            self.next_round = True


import cardhandler
import settings
import pygame


class PlayerUI:
    number_of_players_2 = pygame.image.load(settings.NUMBER_2)
    number_of_players_2 = pygame.transform.scale(number_of_players_2, (50, 50))

    number_of_players_3 = pygame.image.load(settings.NUMBER_3)
    number_of_players_3 = pygame.transform.scale(number_of_players_3, (50, 50))

    number_of_players_4 = pygame.image.load(settings.NUMBER_4)
    number_of_players_4 = pygame.transform.scale(number_of_players_4, (50, 50))

    number_of_players_2_rect = None
    number_of_players_3_rect = None
    number_of_players_4_rect = None

    new_game = None
    number_of_players = 2

    player_uis = []

    hide_all = False
    show_winner = False

    def __init__(self, player, pygame_object, initial_x_pos, initial_y_pos):
        self.hide_player = False
        self.player = player  # orginal player object from model classes
        self.game = pygame_object
        self.cardhandler = cardhandler.CardHandler()
        self.x_pos_card = initial_x_pos
        self.y_pos_card = initial_y_pos
        self.x_offset_card = 70
        self.x_pos_call = initial_x_pos
        self.y_pos_call = initial_y_pos
        self.x_offset_call = 110
        self.x_pos_player = initial_x_pos
        self.y_pos_player = initial_y_pos

        self.load_positions()
        self.call = self.load_call_ui()
        self.fold = self.load_fold_ui()
        self.load_player_cards_ui()
        self.initial_load_done = False
        self.font_player_name = pygame.font.Font('freesansbold.ttf', 40)
        self.font_player_name.italic = True

    def load(self):
        self.load_positions()
        if not PlayerUI.hide_all:
            self.call = self.load_call_ui()
            self.fold = self.load_fold_ui()
            self.load_player_cards_ui()
            self.load_community_cards_ui()
            self.load_player_place_ui()
        if self.show_winner:
            self.show_winner_ui()

    def load_positions(self):
        if self.player.name == "Player 1":
            self.x_pos_card = 250
            self.y_pos_card = 130
            self.x_pos_call = 290
            self.y_pos_call = 240
            self.x_pos_player = 310
            self.y_pos_player = 60

        if self.player.name == "Player 2":
            self.x_pos_card = 250
            self.y_pos_card = 550
            self.x_pos_call = 290
            self.y_pos_call = 510
            self.x_pos_player = 310
            self.y_pos_player = 665

        if self.player.name == "Player 3":
            self.x_pos_card = 500
            self.y_pos_card = 550
            self.x_pos_call = 540
            self.y_pos_call = 510
            self.x_pos_player = 560
            self.y_pos_player = 665

        if self.player.name == "Player 4":
            self.x_pos_card = 500
            self.y_pos_card = 130
            self.x_pos_call = 540
            self.y_pos_call = 240
            self.x_pos_player = 560
            self.y_pos_player = 60

    # load UI cards for the current player here
    def load_player_cards_ui(self):
        card_pos_x = self.x_pos_card  # print(self.player.name)
        for card in self.player.cards:
            card_pos_x += self.x_offset_card
            self.game.screen.blit(self.cardhandler.card_load(card), (card_pos_x, self.y_pos_card))

    def load_community_cards_ui(self):
        community_card_pos_x = 250
        for card in self.game.poker.table.community_cards:
            community_card_pos_x += self.x_offset_card
            self.game.screen.blit(self.cardhandler.card_load(card), (community_card_pos_x, self.y_pos_card + 210))

    def load_call_ui(self):
        if self.hide_player is False:
            call = pygame.draw.rect(self.game.screen, (0, 0, 0), (self.x_pos_call - 10, self.y_pos_call - 7, 100, 40), 2)
            deal_text = self.game.font.render(settings.CALL_TEXT, True, (255, 255, 255))
            self.game.screen.blit(deal_text, (self.x_pos_call, self.y_pos_call))
            return call

    def load_fold_ui(self):
        if self.hide_player is False:
            x_pos_fold = self.x_pos_call + self.x_offset_call
            fold = pygame.draw.rect(self.game.screen, (0, 0, 0), (x_pos_fold - 10, self.y_pos_call - 7, 100, 40), 2)
            fold_text = self.game.font.render(settings.FOLD_TEXT, True, (255, 255, 255))
            self.game.screen.blit(fold_text, (x_pos_fold, self.y_pos_call))
            return fold

    def load_player_place_ui(self):
        x_pos_player = self.x_pos_player
        player_place_text = self.font_player_name.render(self.player.name, True, (0, 0, 255))
        self.game.screen.blit(player_place_text, (x_pos_player, self.y_pos_player))

    def check_current_player_status(self):
        self.player.call = False
        self.player.fold = True

        if self.call.collidepoint(self.game.pos):
            if self.game.clicked:
                print(f"{self.player.name} called")
                self.player.call = True
                self.game.clicked = False

        if self.fold.collidepoint(self.game.pos):
            if self.game.clicked:
                print(f"{self.player.name} folded")
                self.game.poker.folds(self.player.name)
                if len(self.game.poker.table.players) < 2:
                    PlayerUI.show_winner = True
                self.game.clicked = False
                self.hide_player = True

        if self.player.call:
            if not PlayerUI.show_winner:
                try:
                    self.game.poker.__next__()
                    if self.game.poker.rounds == 3:
                        self.game.poker.__next__()
                except StopIteration:
                    print(f"{self.game.poker.winner().name}")
                    PlayerUI.show_winner = True

    def show_winner_ui(self):
        x_pos_winner = 350
        y_pos_winner = 10

        winner_place_text = self.game.font.render(f"Winner   Is   {self.game.poker.winner().name}", True, (0, 0, 0))
        self.game.screen.blit(winner_place_text, (x_pos_winner, y_pos_winner))

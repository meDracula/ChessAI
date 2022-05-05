import sys
import pygame

from poker import Poker
from pokergame import settings
from pokergame.playerui import PlayerUI


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.clicked = False
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.open_game_menu = False
        self.open_number_of_players_menu = False
        self.poker = Poker()
        self.poker.__iter__()
        self.pos = 0

    def load_data(self):
        self.poker_board = pygame.image.load(settings.BOARD)
        self.poker_board = pygame.transform.scale(self.poker_board, (settings.WIDTH, settings.HEIGHT))
        self.menu_icon = pygame.image.load(settings.MENU)

    def new(self):
        pass

    def menu_popup(self):
        pass

        # text = font.render(settings.MENU_TEXT, True, (0, 0, 255))

    def run(self):
        # Game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # Update portion of the game loop
        pass

    def show_initial_player_ui(self):
        x_pos_start = 200
        y_pos_start = 150

        PlayerUI.player_uis.clear()
        for player in self.poker.table.players:
            player_ui = PlayerUI(player, self, x_pos_start, y_pos_start)
            player_ui.load()
            PlayerUI.player_uis.append(player_ui)

    def draw(self):
        self.pos = pygame.mouse.get_pos()

        self.screen.fill(settings.GREEN)
        self.screen.blit(self.poker_board, (0, 0))
        self.screen.blit(self.menu_icon, (10, 10))

        for player_ui in PlayerUI.player_uis:
            player_ui.load()

        if self.menu_icon.get_rect().collidepoint(self.pos) and self.clicked:
            self.open_game_menu = True
            self.clicked = False
            self.open_number_of_players_menu = False

        if self.open_game_menu:
            game_menu = pygame.draw.rect(self.screen, (1, 127, 36), (370, 150, 310, 210), 200)

            leaderboard = pygame.draw.rect(self.screen, (0, 0, 0), (380, 230, 250, 50), 2)
            leaderboard_text = self.font.render(settings.LEADERBOARD, True, (255, 255, 255))
            self.screen.blit(leaderboard_text, (410, 237))

            exit_game = pygame.draw.rect(self.screen, (0, 0, 0), (380, 300, 250, 50), 2)
            exit_text = self.font.render(settings.EXIT_GAME, True, (255, 255, 255))
            self.screen.blit(exit_text, (430, 307))

            exit_menu = pygame.draw.lines(self.screen, (0, 0, 0), False,
                                          ((650, 160), (670, 180), (670, 160), (650, 180),
                                           (650, 160), (670, 160), (650, 180), (670, 180)), 2)

            PlayerUI.new_game = pygame.draw.rect(self.screen, (0, 0, 0), (380, 160, 250, 50), 2)
            new_game_text = self.font.render(settings.NEW_GAME, True, (255, 255, 255))
            self.screen.blit(new_game_text, (430, 167))

            if leaderboard.collidepoint(self.pos):
                if self.clicked:
                    self.clicked = False

            if exit_game.collidepoint(self.pos):
                if self.clicked:
                    self.quit()
                    self.clicked = False

            if exit_menu.collidepoint(self.pos):
                if self.clicked:
                    self.open_game_menu = False
                    self.clicked = False

            if PlayerUI.new_game is not None and PlayerUI.new_game.collidepoint(self.pos):
                if self.clicked:
                    self.open_number_of_players_menu = True
                    PlayerUI.hide_all = True
                    self.clicked = False

        if PlayerUI.new_game is not None and self.open_number_of_players_menu:
            number_of_players_text = self.font.render(settings.NUMBER_OF_PLAYERS, True, (255, 255, 255))
            self.screen.blit(number_of_players_text, (370, 250))

            PlayerUI.number_of_players_2_rect = self.screen.blit(PlayerUI.number_of_players_2, (380, 290, 80, 80))
            PlayerUI.number_of_players_3_rect = self.screen.blit(PlayerUI.number_of_players_3, (480, 290, 80, 80))
            PlayerUI.number_of_players_4_rect = self.screen.blit(PlayerUI.number_of_players_4, (580, 290, 80, 80))

            self.open_game_menu = False

        if PlayerUI.number_of_players_2_rect is not None and PlayerUI.number_of_players_2_rect.collidepoint(self.pos):
            if self.clicked:
                PlayerUI.number_of_players_2_rect = None
                self.open_number_of_players_menu = False
                self.poker.new_game("Player 1", "Player 2")
                self.poker.new_match()
                self.clicked = False
                PlayerUI.number_of_players = 2
                PlayerUI.hide_all = False
                self.show_initial_player_ui()

        if PlayerUI.number_of_players_3_rect is not None and PlayerUI.number_of_players_3_rect.collidepoint(self.pos):
            if self.clicked:
                PlayerUI.number_of_players_3_rect = None
                self.open_number_of_players_menu = False
                self.poker.new_game("Player 1", "Player 2", "Player 3")
                self.poker.new_match()
                self.clicked = False
                PlayerUI.number_of_players = 3
                PlayerUI.hide_all = False
                self.show_initial_player_ui()

        if PlayerUI.number_of_players_4_rect is not None and PlayerUI.number_of_players_4_rect.collidepoint(self.pos):
            if self.clicked:
                PlayerUI.number_of_players_4_rect = None
                self.open_number_of_players_menu = False
                self.poker.new_game("Player 1", "Player 2", "Player 3", "Player 4")
                self.poker.new_match()
                self.clicked = False
                PlayerUI.number_of_players = 4
                PlayerUI.hide_all = False
                self.show_initial_player_ui()

        for player_ui in PlayerUI.player_uis:
            player_ui.check_current_player_status()
        # self.check_player_statuses()  # check the status of all current players in the UI

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicked = True

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    
def main():
    # Create the game Instance
    g = Game()
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_go_screen()


if __name__ == '__main__':
    main()

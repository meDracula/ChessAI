import pygame
from pokergame import settings


class Menu:
    def __init__(self, screen, font):
        self.screen = screen
        self.menu_icon = pygame.image.load(settings.MENU)
        self.font = font

        self.open_game_menu = False
        self.open_number_of_players_menu = False
        self.open_leaderboard = False
        self.open_winner_menu = False

        self.new_game = None
        self.leaderboard = None
        self.exit_game = None
        self.exit_menu = None

    def game_menu(self):
        game_menu = pygame.draw.rect(self.screen, (1, 127, 36), (370, 150, 310, 210), 200)

        self.leaderboard = pygame.draw.rect(self.screen, (0, 0, 0), (380, 230, 250, 50), 2)
        leaderboard_text = self.font.render(settings.LEADERBOARD, True, (255, 255, 255))
        self.screen.blit(leaderboard_text, (410, 237))

        self.exit_game = pygame.draw.rect(self.screen, (0, 0, 0), (380, 300, 250, 50), 2)
        exit_text = self.font.render(settings.EXIT_GAME, True, (255, 255, 255))
        self.screen.blit(exit_text, (430, 307))

        self.exit_menu = pygame.draw.lines(self.screen, (0, 0, 0), False,
                                      ((650, 160), (670, 180), (670, 160), (650, 180),
                                       (650, 160), (670, 160), (650, 180), (670, 180)), 2)

        # New Game box
        self.new_game = pygame.draw.rect(self.screen, (0, 0, 0), (380, 160, 250, 50), 2)
        new_game_text = self.font.render(settings.NEW_GAME, True, (255, 255, 255))
        self.screen.blit(new_game_text, (430, 167))

    def leaderboard(self, top_5):
        self.top_5 = top_5
        pygame.draw.rect(self.screen, (1, 127, 36), (220, 150, 600, 400), 200)
        player = pygame.draw.rect(self.screen, (0, 0, 0), (270, 220, 220, 300), 2)
        cards = pygame.draw.rect(self.screen, (0, 0, 0), (570, 220, 200, 300), 2)

        # player and card text
        player_text = self.font.render("players", True, (0, 0, 255))
        cards_text = self.font.render("cards", True, (0, 0, 255))
        self.screen.blit(player_text, (310, 180))
        self.screen.blit(cards_text, (625, 180))

        # all the players from leaderboard
        first_player = self.font.render(f"{self.top_5[0][0][0]}: {self.top_5[0][0][1]}", True, (0, 0, 255))
        second_player = self.font.render(f"{self.top_5[0][1][0]}: {self.top_5[0][1][1]}", True, (0, 0, 255))
        third_player = self.font.render(f"{self.top_5[0][2][0]}: {self.top_5[0][2][1]}", True, (0, 0, 255))
        fourth_player = self.font.render(f"{self.top_5[0][3][0]}: {self.top_5[0][3][1]}", True, (0, 0, 255))
        fifth_player = self.font.render(f"{self.top_5[0][4][0]}: {self.top_5[0][4][1]}", True, (0, 0, 255))
        self.screen.blit(first_player, (275, 240))
        self.screen.blit(second_player, (275, 290))
        self.screen.blit(third_player, (275, 340))
        self.screen.blit(fourth_player, (275, 390))
        self.screen.blit(fifth_player, (275, 440))

        # all the cards from leaderboard
        first_card = self.font.render(f"{self.top_5[1][0][0]}: {self.top_5[1][0][1]}", True, (0, 0, 255))
        second_card = self.font.render(f"{self.top_5[1][1][0]}: {self.top_5[1][1][1]} ", True, (0, 0, 255))
        third_card = self.font.render(f"{self.top_5[1][2][0]}: {self.top_5[1][2][1]} ", True, (0, 0, 255))
        fourth_card = self.font.render(f"{self.top_5[1][3][0]}: {self.top_5[1][3][1]} ", True, (0, 0, 255))
        fifth_card = self.font.render(f"{self.top_5[1][4][0]}: {self.top_5[1][4][1]} ", True, (0, 0, 255))
        self.screen.blit(first_card, (580, 240))
        self.screen.blit(second_card, (580, 290))
        self.screen.blit(third_card, (580, 340))
        self.screen.blit(fourth_card, (580, 390))
        self.screen.blit(fifth_card, (580, 440))

    def winner_menu(self, winner):
        x_pos_winner = 350
        y_pos_winner = 10
        winner_place_text = self.font.render(f"Winner   Is   {winner['winner'][0]}", True, (0, 0, 0))
        self.screen.blit(winner_place_text, (x_pos_winner, y_pos_winner))


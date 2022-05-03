import sys
import pygame
from poker import Poker
from pokergame import settings
from pokergame.cardhandler import CardHandler
import leaderboard


class Game:
    def __init__(self):
        self.cardhandler = CardHandler()
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.clicked = False
        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.open_game_menu = False
        self.poker = Poker()

    def load_data(self):
        self.poker_board = pygame.image.load(settings.BOARD)
        self.poker_board = pygame.transform.scale(self.poker_board, (settings.WIDTH, settings.HEIGHT))
        self.menu_icon = pygame.image.load(settings.MENU)
        self.top_5 = leaderboard.show_leaderboard()












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

    def draw(self):
        self.poker.new_game('a', 'b', 'c')
        self.poker.new_match()
        pos = pygame.mouse.get_pos()

        self.screen.fill(settings.GREEN)
        self.screen.blit(self.poker_board, (0, 0))
        self.screen.blit(self.menu_icon, (10, 10))
        self.screen.blit(self.cardhandler.card_load('Td'), (300, 120))
        deal = pygame.draw.rect(self.screen, (0, 0, 0), (320, 450, 170, 50), 2)
        call = pygame.draw.rect(self.screen, (0, 0, 0), (320, 450, 170, 50), 2)
        deal_text = self.font.render(settings.CALL_TEXT, True, (0, 0, 255))
        self.screen.blit(deal_text, (360, 460))
        fold = pygame.draw.rect(self.screen, (0, 0, 0), (520, 450, 170, 50), 2)
        fold_text = self.font.render(settings.FOLD_TEXT, True, (0, 0, 255))
        self.screen.blit(fold_text, (560, 460))



        if self.menu_icon.get_rect().collidepoint(pos) and self.clicked:
            self.open_game_menu = True
            self.clicked = False

        if self.open_game_menu:
            game_menu = pygame.draw.rect(self.screen, (1, 127, 36), (370, 220, 310, 210), 200)

            add_opponent = pygame.draw.rect(self.screen, (0, 0, 0), (380, 230, 250, 50), 2)
            add_opponent_text = self.font.render(settings.ADD_OPPONENT, True, (0, 0, 255))
            self.screen.blit(add_opponent_text, (410, 237))

            exit_menu = pygame.draw.lines(self.screen, (0, 0, 0), False,
                                          ((650, 230), (670, 250), (670, 230), (650, 250),
                                           (650, 230), (670, 230), (650, 250), (670, 250)), 2)

            leaderboard = pygame.draw.rect(self.screen, (0, 0, 0), (380, 300, 250, 50), 2)
            leaderboard_text = self.font.render(settings.LEADERBOARD, True, (0, 0, 255))
            self.screen.blit(leaderboard_text, (410, 307))

            exit_game = pygame.draw.rect(self.screen, (0, 0, 0), (380, 370, 250, 50), 2)
            exit_text = self.font.render(settings.EXIT_GAME, True, (0, 0, 255))
            self.screen.blit(exit_text, (430, 377))

            if add_opponent.collidepoint(pos):
                if self.clicked:
                    print("click")
                    self.clicked = False

            if leaderboard.collidepoint(pos):


                if self.clicked:
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

            if exit_game.collidepoint(pos):
                if self.clicked:
                    self.quit()
                    self.clicked = False

            if exit_menu.collidepoint(pos):
                if self.clicked:
                    self.open_game_menu = False
                    self.clicked = False

        for player in self.poker.table.players:
            player.call = False
            player.fold = True

            if call.collidepoint(pos):
                if self.clicked:
                    player.call = True
                    self.clicked = False
            if fold.collidepoint(pos):
                if self.clicked:
                    self.poker.folds(player.name)

            if player.call:
                self.poker.__next__()

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

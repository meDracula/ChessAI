import sys
import pygame
from pokergame import settings
from pokergame.cardhandler import CardHandler


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

    def draw(self):
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

        if call.collidepoint(pos):
            if self.clicked:
                print("hej")
                self.clicked = False
        if fold.collidepoint(pos):
            if self.clicked:
                pass

        if self.menu_icon.get_rect().collidepoint(pos) and self.clicked:
            self.open_game_menu = True
            self.clicked = False



        if self.open_game_menu:
            game_menu = pygame.draw.rect(self.screen, (1, 127, 36), (370, 220, 270, 210), 200)

            add_opponent = pygame.draw.rect(self.screen, (0, 0, 0), (380, 230, 250, 50), 2)
            add_opponent_text = self.font.render(settings.ADD_OPPONENT, True, (0, 0, 255))
            self.screen.blit(add_opponent_text, (410, 237))

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
                    print("click")
                    self.clicked = False

            if exit_game.collidepoint(pos):
                if self.clicked:
                    self.quit()
                    self.clicked = False

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

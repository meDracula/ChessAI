import sys

import pygame
from pokergame import settings


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.clicked = False

    def load_data(self):
        self.poker_board = pygame.image.load(settings.BOARD)
        self.poker_board = pygame.transform.scale(self.poker_board, (settings.WIDTH, settings.HEIGHT))
        self.menu_icon = pygame.image.load(settings.MENU)

    def new(self):
        pass

    def menu_popup(self):

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(settings.MENU_TEXT, True, (0, 0, 255))

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
        if self.menu_icon.get_rect().collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.clicked == False:
                    self.clicked = True
                    print('clicked')
                else:
                    self.clicked = False
            #if pygame.mouse.get_pressed()[0] == 1 and self.clicked == True:
            #    self.clicked = False

        self.screen.fill(settings.GREEN)
        self.screen.blit(self.poker_board, (0, 0))
        self.screen.blit(self.menu_icon, (10, 10))

        if self.clicked:
            rect = pygame.draw.rect(self.screen, (255, 255, 255), (280, 200, 450, 350), 200)

        # self.screen.blit(rect, (200, 200))

        # self.screen.blit(text, (200, 200))
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()

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

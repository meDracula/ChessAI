import sys
import pygame
from pokergame import settings
from pokergame.menu import Menu
from poker import Poker
from pokergame.player import PlayerHandler
from pokergame.cardhandler import CardHandler
from pokergame.leaderboard import show_leaderboard, save_winner
from pokergame.middleman import MiddleMan


class Game:
    def __init__(self, bot: bool):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()

        # Load Data
        self.bot = bot
        self.load_data()

        # Poker package
        self.number_of_players = settings.DEFUALT_AMOUNT_PLAYERS
        self.poker = Poker()

    def load_data(self):
        poker_board = pygame.image.load(settings.BOARD)
        self.poker_board = pygame.transform.scale(poker_board, (settings.WIDTH, settings.HEIGHT))

        self.font = pygame.font.Font('freesansbold.ttf', 30)
        self.menu = Menu(self.screen, self.font)
        self.top_5 = show_leaderboard()

    def new(self):
        names = list(settings.DEFUALT_PLAYER_NAMES)
        if self.bot:
            self.middleman = MiddleMan(settings.DEFUALT_BOT)
            names[self.number_of_players-1] = settings.DEFUALT_BOT

        self.poker.new_game(*names[:self.number_of_players])
        self.cardhandler = CardHandler()
        self.new_match()

    def new_match(self):
        players = self.poker.new_match()

        # Middle man recive the hand
        if self.bot:
            print("="*5, "New Match", "="*5)
            self.middleman.get_hand(players[f'{self.middleman.name}'])
            print(f"Expected outcome {self.poker.exepected_outcome(self.middleman.name)}")

        self.playerhandler = PlayerHandler(players, self.cardhandler)
        self.round = iter(self.poker)

    def run(self):
        # Game loop - set self.playing = False enter show_end_screen
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.menu.menu_icon.get_rect().collidepoint(pos):
                    self.menu.open_game_menu = True

                if self.menu.new_game is not None and self.menu.new_game.collidepoint(pos):
                    # NEW GAME
                    self.menu.open_winner_menu = False
                    self.open_game_menu = False
                    self.new_match()

                if self.menu.leaderboard is not None and self.menu.leaderboard.collidepoint(pos):
                    self.menu.show_leaderboard = True

                if self.menu.exit_game is not None and self.menu.exit_game.collidepoint(pos):
                    self.quit()

                if self.menu.exit_menu is not None and self.menu.exit_menu.collidepoint(pos):
                    self.menu.open_game_menu = False

                if self.playerhandler.call is not None and self.playerhandler.call.collidepoint(pos):
                    self.playerhandler.next_player("call")

                if self.playerhandler.fold is not None and self.playerhandler.fold.collidepoint(pos):
                    self.playerhandler.next_player("fold")

        if self.bot and not self.menu.open_winner_menu and self.playerhandler.current_player == self.middleman.name:
            action = self.middleman.action() if len(self.playerhandler.player_round) > 1 else "call"
            self.playerhandler.next_player(action)

    def update(self):
        if self.playerhandler.next_round and not self.menu.open_winner_menu:
            try:
                if len(self.playerhandler.folds) > 0:
                    self.poker.folds(*self.playerhandler.folds)
                self.community_cards = next(self.round)

                # Middle man revices/update new community_cards
                if self.bot:
                    self.middleman.update_enviroment(self.community_cards, self.playerhandler.folds)

                self.playerhandler.next_round = False
                self.playerhandler.folds = []
            except StopIteration:
                self.winner_is()

    def draw(self):
        # Draw board and floor
        self.screen.fill(settings.GREEN)
        self.screen.blit(self.poker_board, (0, 0))
        self.screen.blit(self.menu.menu_icon, (10, 10))

        # Draw players
        self.playerhandler.draw_players(self)

        # Community cards
        if not self.playerhandler.preflop:
            self.cardhandler.draw_community_cards(self, self.community_cards)

        # Draw action
        if self.playerhandler.previous_act is not None and not self.menu.open_winner_menu:
            line = f"{self.playerhandler.previous_act[0]}   {self.playerhandler.previous_act[1]}"
            action_place_text = self.font.render(line, True, (0, 0, 0))
            self.screen.blit(action_place_text, (350, 10))


        # Show Menu
        if self.menu.open_game_menu:
            self.menu.game_menu()

        # Show leaderboard
        if self.menu.open_leaderboard:
            self.menu.leaderboard(self.top_5)

        # Show Winner Text
        if self.menu.open_winner_menu:
            self.menu.winner_menu(self.winner)
            self.menu.game_menu()

        pygame.display.flip()

    def winner_is(self):
        self.winner = self.poker.winner()
        self.menu.open_winner_menu = True
        save_winner(self.winner)
        self.top_5 = show_leaderboard()

    def show_start_screen(self):
        pass

    def show_end_screen(self):
        pass

def prompt_bot():
    ans = ""
    while True:
        ans = input("BOT? (y/n) > ")
        if ans == "y" or ans == "n":
            break
    return True if ans == "y" else False


def main():
    bot = prompt_bot()
    # Create the game Instance
    g = Game(bot)
    g.show_start_screen()
    while True:
        g.new()
        g.run()
        g.show_end_screen()


if __name__ == '__main__':
    main()

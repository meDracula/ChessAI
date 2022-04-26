import sys

import pygame

from poker.deck import Deck
from pokergame import settings


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.load_data()
        self.clicked = False
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def load_data(self):
        self.poker_board = pygame.image.load(settings.BOARD)
        self.poker_board = pygame.transform.scale(self.poker_board, (settings.WIDTH, settings.HEIGHT))
        self.menu_icon = pygame.image.load(settings.MENU)

        self.Ac = pygame.image.load(settings.ace_of_clubs)
        self.Ac = pygame.transform.scale(self.Ac, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.As = pygame.image.load(settings.ace_of_spades)
        self.As = pygame.transform.scale(self.As, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ah = pygame.image.load(settings.ace_of_hearts)
        self.Ah = pygame.transform.scale(self.Ah, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ad = pygame.image.load(settings.ace_of_diamonds)
        self.Ad = pygame.transform.scale(self.Ad, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ec = pygame.image.load(settings.eight_of_clubs)
        self.Ec = pygame.transform.scale(self.Ec, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Es = pygame.image.load(settings.eight_of_spades)
        self.Es = pygame.transform.scale(self.Es, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Eh = pygame.image.load(settings.eight_of_hearts)
        self.Eh = pygame.transform.scale(self.Eh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ed = pygame.image.load(settings.eight_of_diamonds)
        self.Ed = pygame.transform.scale(self.Ed, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Fc = pygame.image.load(settings.five_of_clubs)
        self.Fc = pygame.transform.scale(self.Fc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Fs = pygame.image.load(settings.five_of_spades)
        self.Fs = pygame.transform.scale(self.Fs, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Fh = pygame.image.load(settings.five_of_hearts)
        self.Fh = pygame.transform.scale(self.Fh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Fd = pygame.image.load(settings.five_of_diamonds)
        self.Fd = pygame.transform.scale(self.Fd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.fc = pygame.image.load(settings.four_of_clubs)
        self.fc = pygame.transform.scale(self.fc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.fs = pygame.image.load(settings.four_of_spades)
        self.fs = pygame.transform.scale(self.fs, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.fh = pygame.image.load(settings.four_of_hearts)
        self.fh = pygame.transform.scale(self.fh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.fd = pygame.image.load(settings.four_of_diamonds)
        self.fd = pygame.transform.scale(self.fd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Jc = pygame.image.load(settings.jack_of_clubs)
        self.Jc = pygame.transform.scale(self.Jc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Js = pygame.image.load(settings.jack_of_spades)
        self.Js = pygame.transform.scale(self.Js, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Jh = pygame.image.load(settings.jack_of_hearts)
        self.Jh = pygame.transform.scale(self.Jh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Jd = pygame.image.load(settings.jack_of_diamonds)
        self.Jd = pygame.transform.scale(self.Jd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Kc = pygame.image.load(settings.king_of_clubs)
        self.Kc = pygame.transform.scale(self.Kc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ks = pygame.image.load(settings.king_of_spades)
        self.Ks = pygame.transform.scale(self.Ks, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Kh = pygame.image.load(settings.king_of_hearts)
        self.Kh = pygame.transform.scale(self.Kh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Kd = pygame.image.load(settings.king_of_diamonds)
        self.Kd = pygame.transform.scale(self.Kd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Nc = pygame.image.load(settings.nine_of_clubs)
        self.Nc = pygame.transform.scale(self.Nc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ns = pygame.image.load(settings.nine_of_spades)
        self.Ns = pygame.transform.scale(self.Ns, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Nh = pygame.image.load(settings.nine_of_hearts)
        self.Nh = pygame.transform.scale(self.Nh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Nd = pygame.image.load(settings.nine_of_diamonds)
        self.Nd = pygame.transform.scale(self.Nd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Qc = pygame.image.load(settings.queen_of_clubs)
        self.Qc = pygame.transform.scale(self.Qc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Qs = pygame.image.load(settings.queen_of_spades)
        self.Qs = pygame.transform.scale(self.Qs, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Qh = pygame.image.load(settings.queen_of_hearts)
        self.Qh = pygame.transform.scale(self.Qh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Qd = pygame.image.load(settings.queen_of_diamonds)
        self.Qd = pygame.transform.scale(self.Qd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Sc = pygame.image.load(settings.seven_of_clubs)
        self.Sc = pygame.transform.scale(self.Sc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ss = pygame.image.load(settings.seven_of_spades)
        self.Ss = pygame.transform.scale(self.Ss, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Sh = pygame.image.load(settings.seven_of_hearts)
        self.Sh = pygame.transform.scale(self.Sh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Sd = pygame.image.load(settings.seven_of_diamonds)
        self.Sd = pygame.transform.scale(self.Sd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.sc = pygame.image.load(settings.six_of_clubs)
        self.sc = pygame.transform.scale(self.sc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.ss = pygame.image.load(settings.six_of_spades)
        self.ss = pygame.transform.scale(self.ss, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.sh = pygame.image.load(settings.six_of_hearts)
        self.sh = pygame.transform.scale(self.sh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.sd = pygame.image.load(settings.six_of_diamonds)
        self.sd = pygame.transform.scale(self.sd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Tc = pygame.image.load(settings.ten_of_clubs)
        self.Tc = pygame.transform.scale(self.Tc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ts = pygame.image.load(settings.ten_of_spades)
        self.Ts = pygame.transform.scale(self.Ts, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Th = pygame.image.load(settings.ten_of_hearts)
        self.Th = pygame.transform.scale(self.Th, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Td = pygame.image.load(settings.ten_of_diamonds)
        self.Td = pygame.transform.scale(self.Td, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Thc = pygame.image.load(settings.three_of_clubs)
        self.Thc = pygame.transform.scale(self.Thc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Ths = pygame.image.load(settings.three_of_spades)
        self.Ths = pygame.transform.scale(self.Ths, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Thh = pygame.image.load(settings.three_of_hearts)
        self.Thh = pygame.transform.scale(self.Thh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Thd = pygame.image.load(settings.three_of_diamonds)
        self.Thd = pygame.transform.scale(self.Thd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Twc = pygame.image.load(settings.two_of_clubs)
        self.Twc = pygame.transform.scale(self.Twc, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Tws = pygame.image.load(settings.two_of_spades)
        self.Tws = pygame.transform.scale(self.Tws, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Twh = pygame.image.load(settings.two_of_hearts)
        self.Twh = pygame.transform.scale(self.Twh, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.Twd = pygame.image.load(settings.two_of_diamonds)
        self.Twd = pygame.transform.scale(self.Twd, (settings.CARDWIDHT, settings.CARDHEIGHT))

        self.cards = {'Ac': self.Ac,
                      'As': self.As,
                      'Ah': self.Ah,
                      'Ad': self.Ad,
                      'Ec': self.Ec,
                      'Es': self.Es,
                      'Eh': self.Eh,
                      'Ed': self.Ed,
                      'Fc': self.Fc,
                      'Fs': self.Fs,
                      'Fh': self.Fh,
                      'Fd': self.Fd,
                      'fc': self.fc,
                      'fs': self.fs,
                      'fh': self.fh,
                      'fd': self.fd,
                      'Jc': self.Jc,
                      'Js': self.Js,
                      'Jh': self.Jh,
                      'Jd': self.Jd,
                      'Kc': self.Kc,
                      'Ks': self.Ks,
                      'Kh': self.Kh,
                      'Kd': self.Kd,
                      'Nc': self.Nc,
                      'Ns': self.Ns,
                      'Nh': self.Nh,
                      'Nd': self.Nd,
                      'Qc': self.Qc,
                      'Qs': self.Qs,
                      'Qh': self.Qh,
                      'Qd': self.Qd,
                      'Sc': self.Sc,
                      'Ss': self.Ss,
                      'Sh': self.Sh,
                      'Sd': self.Sd,
                      'sc': self.sc,
                      'ss': self.ss,
                      'sh': self.sh,
                      'sd': self.sd,
                      'Tc': self.Tc,
                      'Ts': self.Ts,
                      'Th': self.Th,
                      'Td': self.Td,
                      'Thc': self.Thc,
                      'Ths': self.Ths,
                      'Thh': self.Thh,
                      'Thd': self.Thd,
                      'Twc': self.Twc,
                      'Tws': self.Tws,
                      'Twh': self.Twh,
                      'Twd': self.Twd}

        if Deck.init_deck():
            for card in self.cards:
                if card in Deck.init_deck() == 'Ac':  # deck in Deck.init_deck()
                    return self.cards['Ac']
                elif card in Deck.init_deck() == 'As':
                    return self.cards['As']
                elif card in Deck.init_deck() == 'Ah':
                    return self.cards['Ah']
                elif card in Deck.init_deck() == 'Ad':
                    return self.cards['Ad']

                if card in Deck.init_deck() == 'Ec':
                    return self.cards['Ec']
                elif card in Deck.init_deck() == 'Es':
                    return self.cards['Es']
                elif card in Deck.init_deck() == 'Eh':
                    return self.cards['Eh']
                elif card in Deck.init_deck() == 'Ed':
                    return self.cards['Ed']

                if card in Deck.init_deck() == 'Fc':
                    return self.cards['Fc']
                elif card in Deck.init_deck() == 'Fs':
                    return self.cards['Fs']
                elif card in Deck.init_deck() == 'Fh':
                    return self.cards['Fh']
                elif card in Deck.init_deck() == 'Fd':
                    return self.cards['Fd']

                if card in Deck.init_deck() == 'fc':
                    return self.cards['fc']
                elif card in Deck.init_deck() == 'fs':
                    return self.cards['fs']
                elif card in Deck.init_deck() == 'fh':
                    return self.cards['fh']
                elif card in Deck.init_deck() == 'fd':
                    return self.cards['fd']

                if card in Deck.init_deck() == 'Jc':
                    return self.cards['Jc']
                elif card in Deck.init_deck() == 'Js':
                    return self.cards['Js']
                elif card in Deck.init_deck() == 'Jh':
                    return self.cards['Jh']
                elif card in Deck.init_deck() == 'Jd':
                    return self.cards['Jd']

                if card in Deck.init_deck() == 'Kc':
                    return self.cards['Kc']
                elif card in Deck.init_deck() == 'Ks':
                    return self.cards['Ks']
                elif card in Deck.init_deck() == 'Kh':
                    return self.cards['Kh']
                elif card in Deck.init_deck() == 'Kd':
                    return self.cards['Kd']

                if card in Deck.init_deck() == 'Nc':
                    return self.cards['Nc']
                elif card in Deck.init_deck() == 'Ns':
                    return self.cards['Ns']
                elif card in Deck.init_deck() == 'Nh':
                    return self.cards['Nh']
                elif card in Deck.init_deck() == 'Nd':
                    return self.cards['Nd']

                if card in Deck.init_deck() == 'Qc':
                    return self.cards['Qc']
                elif card in Deck.init_deck() == 'Qs':
                    return self.cards['Qs']
                elif card in Deck.init_deck() == 'Qh':
                    return self.cards['Qh']
                elif card in Deck.init_deck() == 'Qd':
                    return self.cards['Qd']

                if card in Deck.init_deck() == 'Sc':
                    return self.cards['Sc']
                elif card in Deck.init_deck() == 'Ss':
                    return self.cards['Ss']
                elif card in Deck.init_deck() == 'Sh':
                    return self.cards['Sh']
                elif card in Deck.init_deck() == 'Sd':
                    return self.cards['Sd']

                if card in Deck.init_deck() == 'sc':
                    return self.cards['sc']
                elif card in Deck.init_deck() == 'ss':
                    return self.cards['ss']
                elif card in Deck.init_deck() == 'sh':
                    return self.cards['sh']
                elif card in Deck.init_deck() == 'sd':
                    return self.cards['sd']

                if card in Deck.init_deck() == 'Tc':
                    return self.cards['Tc']
                elif card in Deck.init_deck() == 'Ts':
                    return self.cards['Ts']
                elif card in Deck.init_deck() == 'Th':
                    return self.cards['Th']
                elif card in Deck.init_deck() == 'Td':
                    return self.cards['Td']

                if card in Deck.init_deck() == 'Thc':
                    return self.cards['Thc']
                elif card in Deck.init_deck() == 'Ths':
                    return self.cards['Ths']
                elif card in Deck.init_deck() == 'Thh':
                    return self.cards['Thh']
                elif card in Deck.init_deck() == 'Thd':
                    return self.cards['Thd']

                if card in Deck.init_deck() == 'Twc':
                    return self.cards['Twc']
                elif card in Deck.init_deck() == 'Tws':
                    return self.cards['Tws']
                elif card in Deck.init_deck() == 'Twh':
                    return self.cards['Twh']
                elif card in Deck.init_deck() == 'Twd':
                    return self.cards['Twd']

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
        if self.menu_icon.get_rect().collidepoint(pos):
            pass
            #if pygame.mouse.get_pressed()[0] == 1:
                #if self.clicked == False:
                 #   self.clicked = True
                 #   print('clicked')
               # else:
                #    self.clicked = False
        print(pygame.mouse.get_pressed()[0], self.menu_icon.get_rect().collidepoint(pos))
        self.screen.fill(settings.GREEN)
        self.screen.blit(self.poker_board, (0, 0))
        self.screen.blit(self.menu_icon, (10, 10))
        self.screen.blit(self.cards['Ac'], (300, 120))
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
        if call.collidepoint(pos):
            if self.clicked:
                pass
        if self.clicked:
            game_menu = pygame.draw.rect(self.screen, (255, 255, 255), (280, 200, 450, 350), 200)

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

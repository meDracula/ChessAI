from pokergame import settings
import pygame


class CardHandler:
    def __init__(self):
        self.cards = {'Ac': settings.ace_of_clubs,
                      'As': settings.ace_of_spades,
                      'Ah': settings.ace_of_hearts,
                      'Ad': settings.ace_of_diamonds,
                      '8c': settings.eight_of_clubs,
                      '8s': settings.eight_of_spades,
                      '8h': settings.eight_of_hearts,
                      '8d': settings.eight_of_diamonds,
                      '5c': settings.five_of_clubs,
                      '5s': settings.five_of_spades,
                      '5h': settings.five_of_hearts,
                      '5d': settings.five_of_diamonds,
                      '4c': settings.four_of_clubs,
                      '4s': settings.four_of_spades,
                      '4h': settings.four_of_hearts,
                      '4d': settings.four_of_diamonds,
                      'Jc': settings.jack_of_clubs,
                      'Js': settings.jack_of_spades,
                      'Jh': settings.jack_of_hearts,
                      'Jd': settings.jack_of_diamonds,
                      'Kc': settings.king_of_clubs,
                      'Ks': settings.king_of_spades,
                      'Kh': settings.king_of_hearts,
                      'Kd': settings.king_of_diamonds,
                      '9c': settings.nine_of_clubs,
                      '9s': settings.nine_of_spades,
                      '9h': settings.nine_of_hearts,
                      '9d': settings.nine_of_diamonds,
                      'Qc': settings.queen_of_clubs,
                      'Qs': settings.queen_of_spades,
                      'Qh': settings.queen_of_hearts,
                      'Qd': settings.queen_of_diamonds,
                      '7c': settings.seven_of_clubs,
                      '7s': settings.seven_of_spades,
                      '7h': settings.seven_of_hearts,
                      '7d': settings.seven_of_diamonds,
                      '6c': settings.six_of_clubs,
                      '6s': settings.six_of_spades,
                      '6h': settings.six_of_hearts,
                      '6d': settings.six_of_diamonds,
                      'Tc': settings.ten_of_clubs,
                      'Ts': settings.ten_of_spades,
                      'Th': settings.ten_of_hearts,
                      'Td': settings.ten_of_diamonds,
                      '3c': settings.three_of_clubs,
                      '3s': settings.three_of_spades,
                      '3h': settings.three_of_hearts,
                      '3d': settings.three_of_diamonds,
                      '2c': settings.two_of_clubs,
                      '2s': settings.two_of_spades,
                      '2h': settings.two_of_hearts,
                      '2d': settings.two_of_diamonds
                    }
        self.loaded_cards = {}

    def card_load(self, card):
        image = pygame.image.load(self.cards[card])
        pycard = pygame.transform.scale(image, (settings.CARDWIDHT, settings.CARDHEIGHT))
        self.loaded_cards[card] = pycard
        return pycard

    def draw_community_cards(self, game, community_cards, offset_x=70):
        community_card_pos_x = 250
        community_card_pos_y = 330
        for card in community_cards['community cards']:
            community_card_pos_x += offset_x
            game.screen.blit(self.loaded_cards.get(card, self.card_load(card)), (community_card_pos_x,
                                                                                 community_card_pos_y))

    def draw_player_cards(self, game, card, pos):
        game.screen.blit(self.loaded_cards.get(card, self.card_load(card)), pos)

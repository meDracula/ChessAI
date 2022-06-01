from os import path
from pokerai.card_compute import card_compute
from pokerai.n_network import NeuralNetwork
import torch

class PokerAI:
    dir_path = "/data/"

    def __init__(self, model):
        self.model = model

    @classmethod
    def load_model(cls, filename="dummy2.ph"):
        full_path = path.abspath(__file__)
        file_path = path.dirname(full_path) + cls.dir_path + filename
        model = NeuralNetwork()
        model.load_state_dict(torch.load(file_path))
        model.eval()
        return PokerAI(model)

    # Pygame
    def get_hand(self, hand):
        # Preflop
        self.computed_hand = [card_compute(hand[0]), card_compute(hand[1])]
        self.X = torch.tensor([self.computed_hand[0], self.computed_hand[1],
                                0, 0, 0, 0, 0], dtype=torch.float)

    def observation(self, community_cards, players_fold):
        community_cards = community_cards['community cards']
        # Flop
        if len(community_cards) == 3:
            self.X = torch.tensor([self.computed_hand[0], self.computed_hand[1],
                                    card_compute(community_cards[0]),
                                    card_compute(community_cards[1]),
                                    card_compute(community_cards[2]),
                                    0, 0], dtype=torch.float)
        # Turn
        elif len(community_cards) == 4:
            self.X = torch.tensor([self.computed_hand[0], self.computed_hand[1],
                                  card_compute(community_cards[0]),
                                  card_compute(community_cards[1]),
                                  card_compute(community_cards[2]),
                                  card_compute(community_cards[3]), 0], dtype=torch.float)
        # River
        else:
            self.X = torch.tensor([self.computed_hand[0], self.computed_hand[1],
                                  card_compute(community_cards[0]),
                                  card_compute(community_cards[1]),
                                  card_compute(community_cards[2]),
                                  card_compute(community_cards[3]),
                                  card_compute(community_cards[4])], dtype=torch.float)

    def clear_outcome_action(self, output):
        print(output, end=" ")
        return "call" if output > 0.5 else "fold"


    def action(self):
        action = self.clear_outcome_action(self.model(self.X))
        print("-> ", action, end="\n")
        return action

    def clear(self):
        print("="*5, "New Match", "="*5)
        self.X = None
        self.computed_hand = None

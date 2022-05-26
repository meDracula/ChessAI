from os import path
from neural_network.n_network import NeuralNetwork
import torch

class PokerAI:
    def __init__(self, model):
        self.model = model

    @classmethod
    def load_model(cls, filename="dummy.ph"):
        full_path = path.abspath(__file__)
        file_path = path.dirname(full_path) + "/training/data/" + filename
        model = NeuralNetwork(11, 64)
        model.load_state_dict(torch.load(file_path))
        model.eval()
        return PokerAI(model)

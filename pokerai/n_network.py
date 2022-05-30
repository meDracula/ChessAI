import torch.nn as nn
import torch.nn.functional as F


class NeuralNetwork(nn.Module):
    def __init__(self, n_inputs=7, n_neurons=20, h_layers=5):
        super().__init__()

        self.activation = nn.Sigmoid()

        # Input layer
        self.input = nn.Linear(n_inputs, n_neurons)

        # Hidden layers
        self.hidden_layer = [nn.Linear(n_neurons, n_neurons) for _ in range(h_layers)]

        # Output layer
        self.output = nn.Linear(n_neurons, 2)

    def forward(self, inputs):
        z = F.relu(self.input(inputs))

        for layer in self.hidden_layer:
            z = F.relu(layer(z))

        output = self.output(z)
        return self.activation(output)

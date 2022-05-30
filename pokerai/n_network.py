import torch.nn as nn
import torch.nn.functional as F


class NeuralNetwork(nn.Module):
    def __init__(self, n_inputs=7, n_neurons=20, h_layers=5):
        super().__init__()

        # Input layer
        self.input = nn.Linear(n_inputs, n_neurons)

        # Hidden layers
        self.hidden_layer = [nn.Linear(n_neurons, n_neurons) for _ in range(h_layers)]

        # Output layer
        self.output = nn.Linear(n_neurons, 2)

        #self.layer_one = nn.Linear(n_neurons, n_neurons)
        #self.layer_two = nn.Linear(n_neurons, n_neurons)
        #self.layer_three = nn.Linear(n_neurons, n_neurons)
        #self.layer_four = nn.Linear(n_neurons, n_neurons)
        #self.layer_five = nn.Linear(n_neurons, n_neurons)

    def forward(self, inputs):
        z = F.relu(self.input(inputs))

        for layer in self.hidden_layer:
            z = F.relu(layer(z))

        output = self.output(z)
        return F.log_softmax(output, dim=0)

        #z = F.relu(self.layer_one(input_value))
        #z = F.relu(self.layer_two(z))
        #z = F.relu(self.layer_three(z))
        #z = F.relu(self.layer_four(z))
        #z = F.relu(self.layer_five(z))

import torch.nn as nn
import torch.nn.functional as F


class NeuralNetwork(nn.Module):
    def __init__(self, n_inputs, n_neurons):
        super().__init__()

        self.input = nn.Linear(n_inputs, n_neurons)

        self.layer_one = nn.Linear(n_neurons, n_neurons)
        self.layer_two = nn.Linear(n_neurons, n_neurons)
        self.layer_three = nn.Linear(n_neurons, n_neurons)
        self.Layer_four = nn.Linear(n_neurons, n_neurons)
        self.layer_five = nn.Linear(n_neurons, n_neurons)

        self.output = nn.Linear(n_neurons, 2)

    def forward(self, inputs):
        input_value = F.relu(self.input(inputs))
        z = F.relu(self.layer_one(input_value))
        z = F.relu(self.layer_two(z))
        z = F.relu(self.layer_three(z))
        z = F.relu(self.layer_four(z))
        z = F.relu(self.layer_five(z))
        output = self.output(z)
        return F.log_softmax(output, dim=0)

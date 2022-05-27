import torch.nn as nn
import torch.nn.functional as F


class NeuralNetwork(nn.Module):
    def __init__(self, n_inputs, n_neurons):
        super().__init__()
        self.input = nn.Linear(n_inputs, n_neurons)

        self.first_hidden = nn.Linear(n_neurons, n_neurons)
        self.second_hidden = nn.Linear(n_neurons, n_neurons)
        self.third_hidden = nn.Linear(n_neurons, n_neurons)
        self.fourth_hidden = nn.Linear(n_neurons, n_neurons)

        self.output = nn.Linear(n_neurons, 2)

    def forward(self, inputs):
        input_value = F.relu(self.input(inputs))
        first = F.relu(self.first_hidden(input_value))
        second = F.relu(self.second_hidden(first))
        third = F.relu(self.third_hidden(second))
        fourth = F.relu(self.fourth_hidden(third))
        output = self.output(fourth)
        # return output
        return F.softmax(output, dim=0)

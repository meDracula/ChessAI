import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

class NeuralNetwork(nn.Module):
    def __init__(self, n_inputs, n_neurons):
        super().__init__()
        # self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        # self.biases = np.zeros((1, n_neurons))

        self.input = nn.Linear(n_inputs, n_neurons)

        self.FC1 = nn.Linear(n_neurons, n_neurons)
        self.FC2 = nn.Linear(n_neurons, n_neurons)
        self.FC3 = nn.Linear(n_neurons, n_neurons)
        self.FC4 = nn.Linear(n_neurons, n_neurons)
        self.FC5 = nn.Linear(n_neurons, n_neurons)

        self.output = nn.Linear(n_neurons, 2)


    def forward(self, inputs):
        # self.output = np.dot(inputs, self.weights) + self.biases
        input_value = F.relu(self.input(inputs))
        z = F.relu(self.FC1(input_value))
        z = F.relu(self.FC2(z))
        z = F.relu(self.FC3(z))
        z = F.relu(self.FC4(z))
        z = F.relu(self.FC5(z))
        output = self.output(z)
        return F.log_softmax(output, dim=0)

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

        self.first_hidden = nn.Linear(n_neurons, n_neurons)
        self.second_hidden = nn.Linear(n_neurons, n_neurons)
        self.third_hidden = nn.Linear(n_neurons, n_neurons)

        self.output = nn.Linear(n_neurons, 2)


    def forward(self, inputs):
        # self.output = np.dot(inputs, self.weights) + self.biases
        input_value = F.relu(self.input(inputs))
        first = F.relu(self.first_hidden(input_value))
        second = F.relu(self.second_hidden(first))
        third = F.relu(self.third_hidden(second))
        output = self.output(third)
        return F.softmax(output, dim=0)





# class ReluActivation:
#     def forward(self, inputs):
#         self.output = np.maximum(0, inputs)
#
#
#
# class SoftmaxActivation:
#     def forward(self, inputs):
#         exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
#         probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
#         self.output = probabilities
#
#
# class Loss:
#     def calculate(self, output, y):
#         sample_losses = self.forward(output, y)
#         data_loss = np.mean(sample_losses)
#         return data_loss
#
#
# class CCLoss(Loss):
#     def forward(selfself, y_pred, y_true):
#         samples = len(y_pred)
#         y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)
#
#         if len(y_true.shape) == 1:
#             correct_confidences = y_pred_clipped[range(samples), y_true]
#         elif len(y_true.shape) == 2:
#             correct_confidences = np.sum(y_pred_clipped * y_true, axis=1)
#         negative_log_likelihoods = -np.log(correct_confidences)
#         return negative_log_likelihoods
#

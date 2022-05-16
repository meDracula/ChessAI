import math

from neural_network.matrix import Matrix




class NeuralNetwork:
    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = Matrix(self.input_nodes, self.hidden_nodes)
        self.weights_ho = Matrix(self.output_nodes, self.hidden_nodes)
        self.weights_ih = Matrix.randomize
        self.weights_ho = Matrix.randomize

        self.bias_h = Matrix(self.hidden_nodes, 1)
        self.bias_o = Matrix(self.output_nodes, 1)
        self.bias_h = Matrix.randomize
        self.bias_o = Matrix.randomize


    def feedforward(self, input_array):
        # generating the hidden outputs
        inputs = Matrix.from_array(input_array)
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.append(self.bias_h)
        # activation function
        hidden.map(self.sigmoid)

        # generating the output's output
        output = Matrix.multiply(self.weights_ho, hidden)
        output.append(self.bias_o)
        output.map(self.sigmoid)

        # sending back to the caller
        return output.to_array()

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

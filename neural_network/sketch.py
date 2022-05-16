from neural_network.n_network import NeuralNetwork


def setup():

    nn = NeuralNetwork(2, 2, 1)
    the_input = [1, 0]
    output = nn.feedforward(the_input)
    print(output)


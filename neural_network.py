import numpy as np


class Node:
    def __init__(self, outdegree):
        self._activation_value = None
        self._weights = None
        self._outdegree = outdegree

    def set_random_weights(self):
        self._weights = np.random.rand(self._outdegree, 1)*0.1


class NeuralNetwork:
    def __init__(self, input_dim, output_dim):
        self._input_dim = input_dim
        self._output_dim = output_dim
        self._hidden_layers_dim = []
        self._layers = None

    def add_layer(self, dim):
        self._hidden_layers_dim.append(dim)

    def build(self):
        layers_dim = [self._input_dim] + self._hidden_layers_dim + [self._output_dim, 0]
        self._layers = []
        for layer_num in range(len(layers_dim) - 1):
            curr_layer_dim = layers_dim[layer_num]
            next_layer_dim = layers_dim[layer_num + 1]

            next_layers = [Node(outdegree=next_layer_dim) for _ in range(curr_layer_dim)]
            self._layers.append(next_layers)

nn = NeuralNetwork(4, 1)
nn.add_layer(5)
nn.add_layer(5)
nn.build()
import numpy as np

np.random.seed(0)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class DenseLayer:
    def __init__(self, n_inputs, n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def ForwardPass(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = DenseLayer(4, 5)
layer2 = DenseLayer(5, 2)
layer3 = DenseLayer(2, 3)

layer1.ForwardPass(X)
layer2.ForwardPass(layer1.output)
layer3.ForwardPass(layer2.output)

print(layer3.output)
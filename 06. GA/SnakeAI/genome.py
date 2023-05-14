'''
Neutron network to predict next step of snake
'''

import numpy as np


class Genome():
    def __init__(self):
        '''
        initial hidden_layer, weight each connection layer
        '''
        self.fitness = 0  # fitness value

        hidden_layer = 10
        # there are 4 hidden layer under each have random node
        # randn(a, b): random a list in each list have b values from 0->1
        # 6(input)->10->20->10->3(output): fully connection
        self.w1 = np.random.randn(6, hidden_layer)  # weight 6->10
        self.w2 = np.random.randn(hidden_layer, 20)  # weight 10->20
        self.w3 = np.random.randn(20, hidden_layer)  # weight 20->10
        self.w4 = np.random.randn(hidden_layer, 3)  # weight 10->3

    def forward(self, inputs: list[float]) -> list[float]:
        '''
        calculate propagation
        '''
        net = np.matmul(inputs, self.w1)
        net = self.relu(net)  # active function
        net = np.matmul(net, self.w2)
        net = self.relu(net)  # active function
        net = np.matmul(net, self.w3)
        net = self.relu(net)  # active function
        net = np.matmul(net, self.w4)
        net = self.softmax(net)  # array have values [0->1] with sum them = 1
        return net

    def relu(self, x):
        return x*(x >= 0)

    def leaky_relu(self, x):
        return np.where(x > 0, x, x * 0.01)

    def softmax(self, x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)


if __name__ == '__main__':
    gen = Genome()
    res = gen.forward([1, 1, 0, 1, 0, 0])

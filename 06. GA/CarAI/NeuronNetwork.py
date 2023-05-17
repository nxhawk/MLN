import numpy as np
import random


class FnActive:
    '''
    All active function for neuron network
    '''

    def __init__(self, func: str = 'sigmoid') -> None:
        self.Fn = self.sigmoid
        self.NameFn = func
        if func == 'tanh':
            self.Fn = self.tanh
        elif func == 'relu':
            self.Fn = self.relu

    def sigmoid(self, x: list[float]):
        '''
        Sigmoid function: f(x) = 1 / (1 + e^(-x))
        '''
        return 1 / (1 + np.exp(-x))

    def tanh(self, x: list[float]):
        '''
        tanh function: f(x) = (e^(x) - e^(-x)) / (e^(x) + e^(-x))
        '''
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def relu(self, x: list[float]):
        '''
        Relu function: f(x) = max (0, x)
        '''
        return 0 if x <= 0 else x

    def calc(self, x: list[float]) -> float:
        '''
        use active function
        '''
        return x if self.NameFn == 'None' else self.Fn(x)

# ---------------------Random weight,bias----------------------


def get_random_weights(size: int, range_: tuple[float, float] = (-1, 1)) -> list[float]:
    '''
    create random weights for connection
    '''
    return [random.uniform(*range_) for _ in range(size)]


def get_random_bias(range_: tuple[float, float] = (-1, 1)) -> float:
    '''
    create random bias for all node in layer
    '''
    return random.uniform(*range_)

# -------------------------------------------------------------


class Neuron:
    '''
    Single neuron object
    '''

    def __init__(self, weights: list[float], bias: float) -> None:
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs: list[float], activation='None'):
        '''
        Propagation predict outputs
        '''
        output = np.dot(self.weights, inputs) + self.bias
        Fnc = FnActive(activation)
        return Fnc.calc(output)


class NeuronNetwork:
    '''
    this network consists of three layers including 1 input layer, 1 hidden layer, and 1 output layer
    input layer has 3 neurons, hidden layer has 5 neurons, and output layer has 2 neurons
    ┌─────────────┬──────────────┬──────────────┐
      input layer  hidden layer  output layer 
    ├─────────────┼──────────────┼──────────────┤
          3             5              2            
    └─────────────┴──────────────┴──────────────┘
    '''

    def __init__(self):
        '''
        fully connected layer
        1 |->    1    |->     
          |->    2    |->     1
        2 |->    3    |->     
          |->    4    |->     2
        3 |->    5    |->     

        3 node input ->5 node hidden->2 output
        '''

        # hidden layer neurons
        # each h is all weight input to this (3 input node)
        self.h1 = Neuron(get_random_weights(3), get_random_bias())
        self.h2 = Neuron(get_random_weights(3), get_random_bias())
        self.h3 = Neuron(get_random_weights(3), get_random_bias())
        self.h4 = Neuron(get_random_weights(3), get_random_bias())
        self.h5 = Neuron(get_random_weights(3), get_random_bias())
        # hidden layer
        self.hs = [self.h1, self.h2, self.h3, self.h4, self.h5]

        # output layer neurons
        # each o is all weight hidden layer to output node (5 hidden node)
        self.o1 = Neuron(get_random_weights(5), get_random_bias())
        self.o2 = Neuron(get_random_weights(5), get_random_bias())
        # outputs
        self.os = [self.o1, self.o2]

        # network's fitness score
        self.score = 0

        # network's accumulative rate calculated by all networks' score
        self.accum_rate = 0

    def feedforward(self, inputs):
        # inputs -> hidden layer
        output_h1 = self.hs[0].feedforward(inputs=inputs)
        output_h2 = self.hs[1].feedforward(inputs=inputs)
        output_h3 = self.hs[2].feedforward(inputs=inputs)
        output_h4 = self.hs[3].feedforward(inputs=inputs)
        output_h5 = self.hs[4].feedforward(inputs=inputs)

        # hidden layer output
        output_h = [output_h1, output_h2, output_h3, output_h4, output_h5]

        # hidden layer -> outputs
        output_o1 = self.os[0].feedforward(output_h, 'tanh')
        output_o2 = self.os[1].feedforward(output_h)
        return [output_o1, output_o2]


def sort_network_by_score(nets: list[NeuronNetwork]) -> list[NeuronNetwork]:
    '''
    sort networks list by their score (fitness), big->small
    '''
    return list(sorted(np.array(nets), key=lambda x: x.score, reverse=True))


def update_network_score(nets: list[NeuronNetwork]) -> list[NeuronNetwork]:
    """
    update every network's score (fitness) per loop
    fitness is determined by every networks' behaves in current round
    """

    # score follow rank this current
    for i in range(len(nets)):
        nets[i].score = i
    return nets


def roulette_selection(nets: list[NeuronNetwork], ratio: float) -> NeuronNetwork:
    '''
    select one network from networks' mating pool by using 'Roulette wheel selection' algorithm
    'roulette' algorithm tend to select one network that has higher score
    '''
    # select k NeuronNetwork
    nets = [nets[i] for i in range(int(len(nets) * ratio))]

    # calculate all networks' total score
    total_score = 0
    for net in nets:
        total_score += net.score

    # calculate every network's accumulative rate
    accum_rate = 0
    for i in range(len(nets)):
        rate = nets[i].score / total_score  # one's probability
        accum_rate += rate
        nets[i].accum_rate = accum_rate

    # select one network randomly by each probability
    n = random.random()
    for net in nets:
        if n < net.accum_rate:
            return net

    return nets[0]


def get_elites(nets: list[NeuronNetwork], ratio: float) -> list:
    """
    get top ratio elites networks from this generation
    """
    elites = [nets[i] for i in range(int(len(nets) * ratio))]
    return elites


def crossover(nets: list[NeuronNetwork], ratio: float) -> NeuronNetwork:
    '''
    select two networks through 'Roulette wheel selection' algorithm,
    then cross their genes (weights) randomly to get a new child (network)
    '''
    father = roulette_selection(nets, ratio)
    mother = roulette_selection(nets, ratio)
    child = NeuronNetwork()

    # crossover hidden layer random_bit_crossover
    for i in range(len(child.hs)):
        if random.random() < 0.5:
            child.hs[i] = father.hs[i]
        else:
            child.hs[i] = mother.hs[i]

    # crossover output layer random_bit_crossover
    for i in range(len(child.os)):
        if random.random() < 0.5:
            child.os[i] = father.os[i]
        else:
            child.os[i] = mother.os[i]

    return child


def mutate(nets: list[NeuronNetwork], pm: float, range_: tuple[float, float]):
    '''
    mutate next generation networks by 'Pm'
    'Pm' is the probability of mutation
    '''

    if not isinstance(nets, list):  # check if list
        for j in range(len(nets.hs)):
            if random.random() < pm:
                # mutate weights and bias
                for k in range(len(nets.hs[j].weights)):
                    nets.hs[j].weights[k] += random.uniform(
                        *range_) * nets.hs[j].weights[k]
                nets.hs[j].bias += random.uniform(*range_) * nets.hs[j].bias
        return nets

    for i in range(len(nets)):
        # every hidden layer's neuron
        for j in range(len(nets[i].hs)):
            if random.random() < pm:
                # mutate weights and bias
                for k in range(len(nets[i].hs[j].weights)):
                    nets[i].hs[j].weights[k] += random.uniform(
                        *range_) * nets[i].hs[j].weights[k]
                nets[i].hs[j].bias += random.uniform(*range_) * \
                    nets[i].hs[j].bias
    return nets


if __name__ == '__main__':
    # test single Neuron
    weights = [1, 2]
    bias = 5
    neuron = Neuron(weights=weights, bias=bias)
    input = [2, 3]
    # print(neuron.feedforward(inputs=input, activation='sigmoid'))

    # test Neuron Network
    network = NeuronNetwork()
    inputs = [20, 3, 4]
    print(network.feedforward(inputs))

    # networks list, every item is a NeuralNetwork
    nets = []

    # initialize networks list, size: 100
    for _ in range(100):
        nets.append(NeuronNetwork())

    # update fitness according to behaves
    nets = update_network_score(nets)

    # sort networks by their fitness
    nets = sort_network_by_score(nets)

    # top 1/4 elite networks
    elites = get_elites(nets, 0.25)

    # next generation's networks list
    next_gen_nets = []

    # add this generation's elites directly to next generation
    next_gen_nets.extend(elites)

    # create hybrid children and add them to next generation until enough
    for _ in range(int(len(nets) / 4 * 3)):
        child = crossover(nets, 0.3)
        next_gen_nets.append(child)

    # mutate next generation's every network including elites
    next_gen_nets = mutate(next_gen_nets, 0.1, (0, 0.1))

    # print([net.hs[1].bias for net in next_gen_nets])

import datetime
import random

geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"
target = "Hello World!!"
startTime = datetime.datetime.now()


class Chromosome:
    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


def get_fitness(guess, target=target):
    return sum(1 for expected, actual in zip(target, guess) if expected == actual)


def _generate_parent(length: int, geneSet: list, get_fitness) -> Chromosome:
    '''
    function to render parent of predict result password

    length: length of result password
    geneSet: list of gene to render answer
    get_fitness: function to caclulate fit
    '''

    genes = []
    while len(genes) < length:
        sampleSize = min(length - len(genes), len(geneSet))
        genes.extend(random.sample(geneSet, sampleSize))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def _mutate(parent: Chromosome, geneSet: list, get_fitness) -> Chromosome:
    random.seed()
    index = random.randrange(0, len(parent.Genes))
    childGenes = list(parent.Genes)
    newGene, alternate = random.sample(geneSet, 2)
    childGenes[index] = alternate if newGene == childGenes[index] else newGene
    genes = ''.join(childGenes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)


def get_best(get_fitness, targetLen: int, optimalFitness: int, geneSet: list, display) -> Chromosome:
    random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)
    if bestParent.Fitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(bestParent, geneSet, get_fitness)
        if bestParent.Fitness >= child.Fitness:
            continue
        display(child)
        if child.Fitness >= optimalFitness:
            return child
        bestParent = child


def display(candidate: Chromosome, startTime: datetime = startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{}\t{}\t{}".format(candidate.Genes, candidate.Fitness, timeDiff))


if __name__ == '__main__':
    RES = get_best(get_fitness, len(target), len(target), geneSet, display)

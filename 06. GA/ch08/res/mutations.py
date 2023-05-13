import random


def swap_mutation(chromosome: list[int], size: int, MUTATION_RATE: float) -> list[int]:
    '''
    Select two positions on the chromosome at random, and interchange the values.
    '''
    size **= 2  # matrix(size*size)

    chromosome_copy = chromosome.copy()
    for i in range(size):
        if random.random() < MUTATION_RATE:
            j = random.randint(0, size - 1)
            chromosome_copy[i], chromosome_copy[j] = chromosome_copy[j], chromosome_copy[i]

    return chromosome_copy

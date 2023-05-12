from random import *

# Note: This method is used for binary numbers!!!


def flip_mutation(chromosome: list[int], size: int) -> list[int]:
    '''
    Flip mutation chooses a random gene in chromosome and flip it.
    If the gene is 0 it will be 1 and else
    '''
    index = randint(0, size - 1)
    chromosome[index] = 1 - chromosome[index]
    return chromosome

# Note: This method is used for binary numbers!!!


def flip_mutation_mask(chromosome: list[int], size: int) -> list[int]:
    """
    Generate a mask of 0s and 1s, then flip the chromosome according to it. If the mask ith gene is 1, the chromosome's
    ith gene will be flipped. the mask ith gene is 0, it won't change anything.
    """
    temp = [randint(0, 1) for _ in range(size)]
    # print(f"Temp chromosome = {temp}")
    for i in range(size):
        if(temp[i] == 1):
            chromosome[i] = 1 - chromosome[i]
    return chromosome

# Note: This method is used for decimal numbers!!!


def divide_mutation(chromosome: list[int], size: int) -> list[int]:
    """
    Choose a random gene in the chromosome and change its valur by dividing it by 2.
    """
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = int(chromosome[index] / 2)
    return chromosome


# Note: This method is used for decimal numbers!!!
def random_reset_mutation(chromosome: list[int], size: int) -> list[int]:
    """
    Choose a random gene and change its value by a value in the same range of chromosome values.
    """
    index = randint(0, size-1)
    # print(f"Index = {index}")
    chromosome[index] = randint(1, size)
    return chromosome


def swap_mutation(chromosome: list[int], size: int) -> list[int]:
    '''
    Select two positions on the chromosome at random, and interchange the values.
    '''
    points = sorted(sample(range(0, size), 2))
    point1 = points[0]
    point2 = points[1]
    # print(f'Swap ({point1}, {point2})')
    # swap this
    chromosome[point1], chromosome[point2] = chromosome[point2], chromosome[point1]
    return chromosome


def scramble_mutation(chromosome: list[int], size: int) -> list[int]:
    '''
    A subset of genes is chosen and their values are scrambled or shuffled randomly.
    '''
    points = sorted(sample(range(0, size), 2))
    point1 = points[0]
    point2 = points[1]

    # print(f'Shuffled ({point1}, {point2})')
    chromosome_shuffle = chromosome[point1:point2 + 1]
    shuffle(chromosome_shuffle)
    chromosome[point1:point2 + 1] = chromosome_shuffle
    return chromosome


def inversion_mutation(chromosome: list[int], size: int) -> list[int]:
    '''
    A subset of genes like in scramble mutation, but instead of shuffling the subset, we merely invert the entire string in the subset.
    '''
    points = sorted(sample(range(0, size), 2))
    point1 = points[0]
    point2 = points[1]

    print(f'Shuffled ({point1}, {point2})')
    chromosome_rev = chromosome[point1:point2 + 1]
    chromosome_rev.reverse()
    chromosome[point1:point2 + 1] = chromosome_rev
    return chromosome

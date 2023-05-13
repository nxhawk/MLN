import random


def _generate_chromosome(size: int) -> list[int]:
    '''
    Generate new random chromosome with sizexsize
    '''
    return random.sample(range(1, size**2 + 1), size**2)


def generate_population(population_size: int, square_size: int) -> list[list[int]]:
    '''
    Generate initial population with population_size
    every chromosome have square_size genes
    '''
    return [_generate_chromosome(square_size) for _ in range(population_size)]

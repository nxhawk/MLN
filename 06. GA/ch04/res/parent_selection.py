from random import *
import numpy as np

# -----------------------------------------------------


# def generate_chromosome(size: int) -> list[int]:
#     """
#     Generates new random chromosome using sample() function from random library.
#     """
#     return sample(range(1, size+1), size)


# def fitness(n: int, chromosome: list[int], max_fitness: int) -> int:
#     conflicts = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
#                 conflicts += 1
#     return int(max_fitness - conflicts)
# ---------------------------------------------------


def roulette_wheel_selection(population: list[list[int]], fitness_values: list[int]) -> list[int]:
    """
    Roulette Wheel is a Parent Selection technique. The chromosome is selected according to its fitness probability.
    The wheel position is generated as a random number between 0 and 1, because we are dealing with probabilities.
    """

    fitness_sum = sum(fitness_values)
    fitness_probs = [(fitness/fitness_sum) for fitness in fitness_values]

    wheel_position = uniform(0, 1)  # random selection probs in 0->1
    comulative_prob = 0

    for index, probs in enumerate(fitness_probs):
        comulative_prob += probs
        if comulative_prob >= wheel_position:
            return population[index]


# -----------------------------------------------------------------------------------

def tournament_selection(population: list[list[int]], fitness_values: list[int], k: int = 0) -> list[int]:
    '''
    Tournament Selection function
    select k population and sort desc (follow fitness) them choose first res
    '''

    if k <= 0:
        k = randint(5, 20)
    # print(f"k = {k}")

    list_of_them = list(zip(population, fitness_values)
                        )  # ->list[[chromosome, int]]
    tournament = choices(list_of_them, k=k)  # select random k tuples
    # sort desc follow fitness
    tournament = sorted(tournament, key=lambda x: x[1], reverse=True)

    return tournament[0][0]  # return max

# -----------------------------------------------------------------------------------


def rank_selection(population: list[list[int]], fitness_values: list[int]) -> list[int]:
    '''
    sort population desc follow fitness_value of them
    assign rank (1->...) to each individual based on position in sorted list
    generate a random number between 1 and rank sum
    select chromosome with sum rank to it > random number 
    '''

    # ->list[[chromosome, int]]
    list_of_them = list(zip(population, fitness_values))

    # sort population by fitness in descending order
    list_of_them = sorted(list_of_them, key=lambda x: x[1], reverse=True)

    n = len(list_of_them)
    # calculate total rank sum
    rank_sum = n * (n + 1) // 2
    # generate a random number between 1 and rank sum
    rand_num = randint(1, rank_sum)  # random max sum rank

    current_sum_rank = 0

    # loop through individuals and accumulate rank sum until random number is reached
    for rank, chromosome in enumerate(list_of_them):
        current_sum_rank += rank + 1
        if current_sum_rank > rand_num:  # over rand_num
            return chromosome[0]  # chromosome
# -----------------------------------------------------------------------------------


def boltzmann_selection(population: list[list[int]], fitness_values: list[int]) -> list[int]:
    '''
    follow sigmon function to render probility
    '''
    T = len(population)
    fitness = np.array(fitness_values)
    prob = np.exp(fitness / T) / np.sum(np.exp(fitness / T))
    chosen_index = np.random.choice(len(population), p=prob)
    return population[chosen_index]

# -----------------------------------------------------------------------------------


def random_selection(population: list[list[int]], fitness_values: list[int]) -> list[int]:
    '''
    choose random parent in population and return this
    '''
    return population[randint(0, len(population) - 1)]


def random_selection_advence(population: list[list[int]], fitness_values: list[int]) -> list[int]:
    '''
    choose parent with sum of (fitness) over than random max sum fitness
    '''
    total_fitness = sum(fitness_values)

    # render random max sum fitness
    rand_val = uniform(0, total_fitness)

    fitness_sum = 0
    for index, fitness in enumerate(fitness_values):
        fitness_sum += fitness
        if fitness_sum >= rand_val:
            return population[index]


# -----------------------------------------------------------------------------------


def stochastic_universal_sampling():
    pass


# if __name__ == '__main__':
#     n = 8
#     POPULATION_SIZE = 200
#     max_fitness = n*(n-1)//2

#     population = [generate_chromosome(n) for _ in range(POPULATION_SIZE)]
#     fitness_values = [fitness(n, chromosome, max_fitness)
#                       for chromosome in population]

#     parent = random_selection_advence(population, fitness_values)
#     print(parent)

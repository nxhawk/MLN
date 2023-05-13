from random import *


def tournament_selection(population: list[list[int]], fitness_values: list[int], k: int) -> tuple[list[list[int]], list[int]]:
    '''
    Tournament Selection function
    select k population and sort desc (follow fitness) them choose first res
    '''

    list_of_them = list(zip(population, fitness_values)
                        )  # ->list[[chromosome, int]]
    # sort desc follow fitness
    list_of_them = sorted(list_of_them, key=lambda x: x[1])

    res1 = []
    res2 = []
    for i in range(k):
        res1.append(list_of_them[i][0])
        res2.append(list_of_them[i][1])

    for _ in range(6):
        rand_num = randint(k + 1, len(population) - 1)
        res1.append(list_of_them[rand_num][0])
        res2.append(list_of_them[rand_num][1])

    return res1, res2


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

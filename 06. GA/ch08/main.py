import numpy as np

from constants import *

from res.chromosomes import *
from res.crossovers import *
from res.mutations import *
from res.parent_selection import *


def calculate_fitness(chromosome: list[int], size: int) -> int:
    '''
    Calculate fitness of a chromosome
    '''

    # reshape from list[int](sizexsize) to matrix[size, size] to calculate fitness
    matrix = np.array(chromosome).reshape((size, size))
    # print(matrix)

    # prepare initial sum (first row) to compare
    target_sum = np.sum(matrix[0, :])

    # axis = 1 sum in row, axis = 0 sum in column
    # sum all column, row, duong cheo chinh, phu - target_sum*(size*2+2)
    return np.sum(np.abs(np.sum(matrix, axis=1) - target_sum)) +\
        np.sum(np.abs(np.sum(matrix, axis=0) - target_sum)) +\
        np.abs(np.trace(matrix) - target_sum) +\
        np.abs(np.trace(np.fliplr(matrix)) - target_sum)

# Select individuals for the next generation using tournament selection


def selection(population: list[list[int]], fitness_scores: list[int], elite_size: float, square_size: int):
    # number of parent as a new generation
    elite_count = int(len(population) * elite_size)

    # tournament selection
    new_generation, fitness_scores = tournament_selection(
        population, fitness_values=fitness_scores, k=elite_count)

    # new offspring
    offspring = new_generation.copy()

    while len(offspring) < len(population):
        # parent selection
        parent1 = roulette_wheel_selection(new_generation, fitness_scores)
        parent2 = roulette_wheel_selection(new_generation, fitness_scores)

        # crossover
        child1, child2 = one_point_crossover(parent1, parent2, square_size)

        # mutation
        child1 = swap_mutation(child1, square_size,
                               MUTATION_RATE=MUTATION_RATE)
        child2 = swap_mutation(child2, square_size,
                               MUTATION_RATE=MUTATION_RATE)

        # new child
        offspring.extend([child1, child2])

    return offspring


if __name__ == '__main__':
    size = int(input("Enter the size of the square: "))
    if size <= 2:
        print(f"Don't solve with size = {size}")
        exit()

    population = generate_population(POPULATION_NUMBERS, size)
    fitness_values = [calculate_fitness(
        chromosome, size) for chromosome in population]

    # initial res
    min_index = np.argmin(np.array(fitness_values))
    cost = fitness_values[min_index]
    chromo = population[min_index]

    for generation in range(GENERATION_NUMBERS):
        population = selection(population, fitness_values, ELITE_PERCENT, size)
        fitness_values = [calculate_fitness(
            chromosome, size) for chromosome in population]

        # find index have min fitness values
        min_index = np.argmin(np.array(fitness_values))
        # print(
        #     f"Generation {generation+1}: Best Fitness = {fitness_values[min_index]}")
        # print(np.array(population[min_index]).reshape((size, size)))
        # print()
        print(
            f"Generation {generation+1}: Best Fitness = {fitness_values[min_index]}")

        if fitness_values[min_index] < cost:
            cost = fitness_values[min_index]
            chromo = population[min_index]

        if cost <= 0:
            print(
                f"\nFinal solution for {size}x{size} magic-board after {generation + 1} generation:\nBest Fitness = {cost}\nBoard:")
            print(np.array(chromo).reshape((size, size)))
            print()
            exit()

    print(f"\nAfter {GENERATION_NUMBERS} generation, Best solution for {size}x{size} magic-board: \nBest Fitness = {cost}\nBoard:")
    print(np.array(chromo).reshape((size, size)))
    print()

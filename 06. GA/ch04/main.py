from ui.UI import *

from res.chromosomes import *
from constants import *

# Main screen to draw on it
win = Screen()
win.title("N-Queen Problem")
win.bgcolor("#dfe6dc")
win.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
win.tracer(0)
win.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)


def fitness(n: int, chromosome: list[int], max_fitness: int) -> int:
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == j - i:
                conflicts += 1
    return int(max_fitness - conflicts)


if __name__ == '__main__':
    # read input n queens
    n = read_input(win)

    if n != 2 and n != 3:  # check if can be solved
        max_fitness = n*(n-1)//2  # high value fitness (as infinity value)

        # Generate the initial population -> list[list[int]]
        population = [generate_chromosome(n) for _ in range(POPULATION_SIZE)]

        # Evaluate the fitness value for each chromosome -> list[int]
        fitness_values = [fitness(n, chromosome, max_fitness)
                          for chromosome in population]

        # Save the fittest found chromosome, it's used when there is no solution found -> list[int]
        fittest_found = population[fitness_values.index(max(fitness_values))]

        generation = 0  # generation start with parent -> 0

        # render new generation under max_generation to find generation have fitmess(chromosome) = max_fitness
        while generation < GENERATIONS_NUMBER and max_fitness != fitness(n, fittest_found, max_fitness):
            population = generate_population(
                POPULATION_SIZE, n, MUTATION_PROBABILITY, population, fitness_values)
            # re calculate fitness_values of new population
            fitness_values = [fitness(n, chromosome, max_fitness)
                              for chromosome in population]

            # Check if the fittest one in the current population is more fit than the saved one
            current_fittest = population[fitness_values.index(
                max(fitness_values))]
            if fitness(n, current_fittest, max_fitness) > fitness(n, fittest_found, max_fitness):
                fittest_found = current_fittest

            # new generation
            generation += 1
        if max_fitness in fitness_values:
            print(f"Solved in generation {generation}")
            solution = fittest_found
            print(
                f"Found solution = {solution} and fitness = {fitness(n, fittest_found, max_fitness)}")

            # show solution
            sc2_solution(generation)
            sc2(n, solution)
        else:
            print(
                f"No solution is found in {GENERATIONS_NUMBER} generations!!")
            print(
                f"Fittest found solution = {fittest_found} and fitness = {fitness(n, fittest_found, max_fitness)}")

            # Use Turtle to show the solution
            sc2_limit(generation, fitness(n, fittest_found, max_fitness))
            sc2(n, fittest_found)
    else:
        print(f"Sorry, the problem can't be solved when N = {n}")
        no_solution(n)

    update()
    done()

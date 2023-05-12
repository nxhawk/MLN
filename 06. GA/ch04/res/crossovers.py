from random import *
# from chromosomes import generate_chromosome


def one_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose a random cut point and swap the parents' portion after the cut point.
    """
    point = randint(1, size - 2)
    # print(f"Point = {point}")

    child1 = chromosome1[:point] + chromosome2[point:]
    child2 = chromosome2[:point] + chromosome1[point:]

    return child1, child2


def two_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose 2 random cut points and swap the parents' portion between those cut points.
    """

    points = sorted(sample(range(1, size), 2))
    point1 = points[0]
    point2 = points[1]
    # print(f"Point1 = {point1}, Point2 = {point2}")

    child1 = chromosome1[:point1] + \
        chromosome2[point1:point2] + chromosome1[point2:]
    child2 = chromosome2[:point1] + \
        chromosome1[point1:point2] + chromosome2[point2:]

    return child1, child2


def mutil_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int, num_of_points: int = 0) -> tuple[list[int], list[int]]:
    """
    Choose n random cut points, where n is also a random number. It alternates between swapping the parents' portion
    between the points, or leave it as it is.
    num_of_points: default = 0(<=0) If you want this number is random
    """
    if num_of_points <= 0:
        num_of_points = randint(1, size - 2)
    points = sorted(sample(range(1, size), num_of_points))
    # print(f"Number of points = {num_of_points}, Points = {points}")

    child1 = chromosome1.copy()
    child2 = chromosome2.copy()

    for i in range(num_of_points - 1):
        child1[points[i]:points[i+1]] = chromosome2[points[i]:points[i+1]]
        child2[points[i]:points[i+1]] = chromosome1[points[i]:points[i+1]]

    return child1, child2


def uniform_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Genrate a mask of 0s and 1s (length = size), and use it to know if we should swap genes or not. If the mask ith gene is 0,
    child1[i], child2[i] = parent2[i],parent1[i] else  
    child1[i], child2[i] = parent1[i],parent2[i]  
    """
    mask = choices([0, 1], k=size)
    # print(f"Mask = {mask}")
    child1 = chromosome1.copy()
    child2 = chromosome2.copy()

    for i in range(size):
        if(mask[i] == 0):
            child1[i] = chromosome2[i]
            child2[i] = chromosome1[i]

    return child1, child2


def uniform_crossover_probability(chromosome1: list[int], chromosome2: list[int], size: int, crossover_probability: float = 0.5) -> tuple[list[int], list[int]]:
    """
    uniform_crossover but use probability to decision
    """
    child1 = chromosome1.copy()
    child2 = chromosome2.copy()

    for i in range(size):
        if random() < crossover_probability:
            child1[i] = chromosome2[i]
            child2[i] = chromosome1[i]

    return child1, child2


if __name__ == '__main__':
    size = 20
    child1 = generate_chromosome(size)
    child2 = generate_chromosome(size)
    print(child1)
    print(child2)
    child1, child2 = uniform_crossover(child1, child2, size)
    print(child1)
    print(child2)

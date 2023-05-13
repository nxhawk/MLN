from random import *


def one_point_crossover(chromosome1: list[int], chromosome2: list[int], size: int) -> tuple[list[int], list[int]]:
    """
    Choose a random cut point and swap the parents' portion after the cut point.
    """
    point = randint(1, size**2 - 2)
    # print(f"Point = {point}")

    child1 = chromosome1[:point] + \
        [gene for gene in chromosome2 if gene not in chromosome1[:point]]
    child2 = chromosome2[:point] + \
        [gene for gene in chromosome1 if gene not in chromosome2[:point]]

    return child1, child2

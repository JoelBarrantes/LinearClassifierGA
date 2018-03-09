
import random
import numpy as np


def mutate(individual, mutation_rate):
    mutation_factor = random.uniform(0, 1)
    if mutation_factor< mutation_rate:
        mutation_c(individual)

def mutation_a(individual):
    i = random.randrange(len(individual.phenotype))
    j = random.randrange(len(individual.phenotype[0]))
    change = random.uniform(0, 1)
    individual.phenotype[i][j] = change

def mutation_b(individual):
    individual.phenotype = np.flip(individual.phenotype, 1)


def mutation_c(individual):
    i = random.randrange(len(individual.phenotype))
    (x, y) = individual.phenotype.shape
    change = np.random.rand(1, y)
    individual.phenotype[i,:] = change

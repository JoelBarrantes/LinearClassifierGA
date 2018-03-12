from Individual import Individual


def cross(parent_a, parent_b, c_function):
    if c_function == "a":
        return crossover_a(parent_a, parent_b)
    else:
        return crossover_b(parent_a, parent_b)


def crossover_a(parent_a, parent_b):
    (x, y) = parent_a.phenotype.shape
    child_a = Individual(0, 1, x, y)
    child_b = Individual(0, 1, x, y)
    for i in range(0, x):
        t = True
        for j in range(0, y):
            if t:
                child_a.phenotype[i, j] = parent_a.phenotype[i, j]
                child_b.phenotype[i, j] = parent_b.phenotype[i, j]
                t = False
            else:
                child_a.phenotype[i, j] = parent_b.phenotype[i, j]
                child_b.phenotype[i, j] = parent_a.phenotype[i, j]
                t = True
    return child_a, child_b


def crossover_b(parent_a, parent_b):
    (x, y) = parent_a.phenotype.shape
    child_a = Individual(0, 1, x, y)
    child_b = Individual(0, 1, x, y)
    t = True
    for i in range(0, x):
        if t:
            child_a.phenotype[i, :] = parent_a.phenotype[i, :]
            child_b.phenotype[i, :] = parent_b.phenotype[i, :]
            t = False
        else:
            child_a.phenotype[i, :] = parent_b.phenotype[i, :]
            child_b.phenotype[i, :] = parent_a.phenotype[i, :]
            t = True
    return child_a, child_b

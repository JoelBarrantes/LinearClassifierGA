from GaAlgorithm import GaAlgorithm
from Settings import Settings


def main():
    # Problem type: 1 is CIFAR, 2 is IRIS
    settings = Settings(1)

    # Hyperparameters
    settings.maxIndividuals = 100
    settings.maxGenerations = 10
    settings.mutation_rate = 0.05
    settings.crossover_rate = 0.7

    elite_percentage = 0.3
    settings.selection_threshold = round(elite_percentage * settings.maxIndividuals)

    # There are two types of fitness: "loss" and "accuracy"
    settings.fitness_function = "loss"

    # There are two types of crossover: "a" and "b"
    settings.crossover_function = "a"

    # There are three types of mutation: "a", "b" and "c"
    settings.mutation_function = "a"

    # Parameters for the normal distribution
    settings.mu = 0
    settings.sigma = 1

    ga_run = GaAlgorithm(settings)

    if __name__ == "__main__":
        ga_run.run()


main()

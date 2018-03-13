import sys
from time import gmtime, strftime

from GaAlgorithm import GaAlgorithm
from Settings import Settings


def main():
    if len(sys.argv) >= 7:
        problem = sys.argv[1]
        maxInd = sys.argv[2]
        maxGen = sys.argv[3]
        mut_rate = sys.argv[4]
        fitness_f = sys.argv[5]
        if sys.argv[6] == 't':
            debug = True
        else:
            debug = False


    else:
        problem = 2
        maxInd = 25
        maxGen = 10
        mut_rate = 5
        fitness_f = "loss"
        debug = False

    # Problem type: 1 is CIFAR, 2 is IRIS

    settings = Settings(int(problem))
    settings.debug_info = debug

    # Hyperparameters
    settings.maxIndividuals = int(maxInd)
    settings.maxGenerations = int(maxGen)
    settings.mutation_rate = int(mut_rate) / 100
    settings.crossover_rate = 0.5

    elite_percentage = 0.3
    settings.selection_threshold = round(elite_percentage * settings.maxIndividuals)

    # There are two types of fitness: "loss" and "accuracy"
    settings.fitness_function = fitness_f

    # There are two types of crossover: "a" and "b"
    settings.crossover_function = "a"

    # There are three types of mutation: "a", "b" and "c"
    settings.mutation_function = "a"

    # Parameters for the normal distribution
    settings.mu = 0
    settings.sigma = 1

    settings.debug = debug
    ga_run = GaAlgorithm(settings)

    if __name__ == "__main__":
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        ga_run.run()
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


main()

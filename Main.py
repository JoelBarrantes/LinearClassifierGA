from GaAlgorithm import GaAlgorithm
from Settings import Settings
from time import gmtime, strftime
import sys

def main():

    problem = sys.argv[1]
    maxInd = sys.argv[2]
    mut_rate = sys.argv[3]
    fitness_f = sys.argv[4]

    # Problem type: 1 is CIFAR, 2 is IRIS
    settings = Settings(int(problem))

    # Hyperparameters
    settings.maxIndividuals = int(maxInd)
    settings.maxGenerations = 10
    settings.mutation_rate = int(mut_rate)/100
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

    ga_run = GaAlgorithm(settings)

    if __name__ == "__main__":
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        ga_run.run()
        print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

main()

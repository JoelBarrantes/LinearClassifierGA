from IrisLoader import load_Iris
from CifarLoader import load_gray_Cifar
import numpy as np

class Settings:

    maxGenerations = 0
    maxIndividuals = 0
    mutation_rate = 0
    selection_threshold = 0

    #Limit for the weight values
    mu = 0
    sigma = 0

    #Gaussian strength
    scale = 0
    size_x = 0
    size_y = 0

    crossover_technique = 0

    #problem type

    problem_type = None
    training_set = None
    labels = None

    def __init__(self, pProblem_type):
        self.problem_type = pProblem_type
        self.load_dataset()

    def load_dataset(self):

        if self.problem_type == 1:
            (self.training_set, self.labels) = load_gray_Cifar()
            self.size_x = 4
            self.size_y = 1025

        if self.problem_type == 2:
            (self.training_set, self.labels) = load_Iris()

            self.size_x = 3
            self.size_y = 5



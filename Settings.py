from CifarLoader import load_gray_cifar
from IrisLoader import load_iris


class Settings:
    # Hyperparameters
    maxGenerations = 0
    maxIndividuals = 0
    mutation_rate = 0
    selection_threshold = 0
    crossover_rate = 0.5
    fitness_function = ""
    crossover_function = "a"
    mutation_function = "a"

    # Limit for the weight values
    mu = 0
    sigma = 0

    # Gaussian strength
    scale = 0
    size_x = 0
    size_y = 0

    # problem type
    problem_type = None
    training_set = None
    labels = None
    save_folder = ""
    debug_info = False
    def __init__(self, pProblem_type):
        self.problem_type = pProblem_type
        self.load_dataset()

    def load_dataset(self):

        if self.problem_type == 1:
            (self.training_set, self.labels) = load_gray_cifar()
            self.size_x = 4
            self.size_y = 1025
            self.save_folder = "cifar/"
        if self.problem_type == 2:
            (self.training_set, self.labels) = load_iris()

            self.size_x = 3
            self.size_y = 5
            self.save_folder = "iris/"

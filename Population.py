from Individual import Individual


class Population:

    individuals_set = []
    maxIndividuals = 0
    mu = 0
    sigma = 0
    scale = 0
    size_x = 0
    size_y = 0


    def __init__(self, pmu, psigma, px, py, pmaxIndividuals):

        self.maxIndividuals = pmaxIndividuals
        self.individuals_set = []
        self.mu = pmu
        self.sigma = psigma
        self.size_x = px
        self.size_y = py

    def initialize_population(self):
        for i in range (0, self.maxIndividuals):

            individual = Individual(self.mu, self.sigma,
                                    self.size_x, self.size_y)

            self.individuals_set.append(individual)


    def get_average_accuracy(self):
        avg_acc = 0
        for item in self.individuals_set:
            avg_acc += item.accuracy
        return avg_acc/self.maxIndividuals


    def get_average_loss(self):
        avg_loss = 0
        for item in self.individuals_set:
            avg_loss += item.loss
        return avg_loss/self.maxIndividuals

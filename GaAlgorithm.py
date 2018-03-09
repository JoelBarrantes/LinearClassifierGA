from multiprocessing import Pool
from multiprocessing import Process
from Population import Population
from Fitness import calculate_fitness
from Crossover import *
from Mutation import *
import scipy.io as sio
import random


class GaAlgorithm:

    settings = None
    population = None
    safebox = []

    def __init__(self, pSettings):
        self.settings = pSettings
        self.population = Population(self.settings.mu, self.settings.sigma,
                                     self.settings.size_x, self.settings.size_y,
                                     self.settings.maxIndividuals)
        self.population.initialize_population()

    def evaluate_population(self):
        limit = self.settings.maxIndividuals

        # with Pool(4) as p:
        #    results = p.starmap(calculate_fitness,[(x, self.settings.problem_type, self.population.individuals_set[x],
        #                           self.settings.training_set, self.settings.labels) for x in range(0,limit)])
        #
        # results.sort(key=lambda tup: tup[0])
        #
        # for i in range(0, limit):
        #    item = results[i]
        #    self.population.individuals_set[i].loss = item[1]
        #    self.population.individuals_set[i].accuracy = item[2]

        #Non parallel implementation
        for i in range(0,limit):
            (i,loss, acc) = calculate_fitness(i,self.settings.problem_type, self.population.individuals_set[i],
                                        self.settings.training_set, self.settings.labels)
            self.population.individuals_set[i].accuracy = acc
            self.population.individuals_set[i].loss = loss

    def run(self):
        gen = self.settings.maxGenerations
        for i in range(0, gen):
            print("Generation ", i)
            self.evaluate_population()
            self.population.individuals_set.sort(key=lambda x: x.loss, reverse=False)
            self.safebox.append((i,int(self.population.individuals_set[0].accuracy *1000 // 1 )
                                 ,self.population.individuals_set[0]))

            print("Metrics: ")
            print("Average accuracy of the population: ", self.population.get_average_accuracy())
            print("Average loss of the population: ", self.population.get_average_loss())

            self.population = self.new_population()
            print("---------------------------------------------------")
        self.evaluate_population()
        self.population.individuals_set.sort(key=lambda x: x.loss, reverse=False)

        self.safebox.append((gen,int(self.population.individuals_set[0].accuracy *1000 // 1 )
                                 ,self.population.individuals_set[0]))
        print("Metrics: ")
        print("Average accuracy of the population: ", self.population.get_average_accuracy())
        print("Average loss of the population: ", self.population.get_average_loss())
        print("Best Individual Accuracy | Loss: ", self.population.individuals_set[0].accuracy,
              self.population.individuals_set[0].loss)

        self.save_safebox()

    def new_population(self):
        new_population = Population(self.settings.mu, self.settings.sigma,
                                     self.settings.size_x, self.settings.size_y,
                                     self.settings.maxIndividuals)
        #Sort by fitness
        elite = self.population.individuals_set[:self.settings.selection_threshold]
        new_population.individuals_set.extend(elite)

        i = self.settings.selection_threshold
        while i < self.settings.maxIndividuals:
            c = random.uniform(0,1)

            if c <= self.settings.crossover_rate:

                child_q = 2
                if i == self.settings.maxIndividuals - 1:
                    child_q = 1

                children = self.get_children(child_q)
                new_population.individuals_set.extend(children)
                i += 2
            else:
                new_individual = Individual(self.settings.mu, self.settings.sigma,
                                            self.settings.size_x, self.settings.size_y)
                new_population.individuals_set.append(new_individual)
                i += 1
        return new_population

    def get_children(self,limit):

        children = []
        while limit > 0:
            par_a = self.get_parent()
            par_b = self.get_parent()

            while True:
                if np.array_equal(par_a.phenotype, par_b.phenotype):
                    par_b = self.get_parent()
                else:
                    break

            (child_a, child_b) = cross(par_a, par_b)
            children.append(child_a)

            if limit != 1:
                children.append(child_b)
            limit -= 2

        return children

    def get_parent(self):
        candidates = self.population.individuals_set
        acc_fitness = 0
        acc_probabilites = 0
        probabilities = []
        for individual in candidates:
            acc_fitness += individual.accuracy

        for individual in candidates:
            p_i = individual.accuracy/acc_fitness
            acc_probabilites += p_i
            probabilities.append(acc_probabilites)

        index = random.uniform(0, 1)
        for i in range(0,len(probabilities)):
            top = probabilities[i]
            if index <= top:
                parent = candidates[i]
                break

        return parent

    def save_safebox(self):
        for item in self.safebox:
            mat = item[2].phenotype
            id = hash(item[2].accuracy+item[2].loss)
            folder = "results/"
            sio.savemat(folder + str(item[0])+"_"+str(item[1])+"_"+str(id)+".mat", {'mat':mat})

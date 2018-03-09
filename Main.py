from Settings import Settings
from GaAlgorithm import GaAlgorithm
from time import gmtime, strftime

def main():
    settings = Settings(1)
    settings.maxIndividuals = 20
    settings.maxGenerations = 10
    settings.mu = 0
    settings.sigma = 1
    settings.mutation_rate = 0.25
    settings.selection_threshold = round(0.3 * settings.maxIndividuals)

    ga_run = GaAlgorithm(settings)
    if __name__ == "__main__":
        ga_run.run()


print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
main()
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

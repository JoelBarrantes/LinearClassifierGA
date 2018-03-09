import numpy as np

class Individual:

    phenotype = None
    accuracy = 0
    loss = 0

    def __init__(self, mu, sigma, x, y):
        #self.phenotype = np.random.rand(x, y)
        self.phenotype = np.random.normal(mu,sigma, (x,y))


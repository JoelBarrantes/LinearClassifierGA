
from sklearn.datasets import load_iris
import numpy as np


def load_Iris():
    new_train_set= []
    iris = load_iris()
    # Arreglos de numpy
    train_data = iris.data
    train_labels = iris.target

    for item in train_data:
        new_train_set.append(item)

    return (new_train_set, train_labels)

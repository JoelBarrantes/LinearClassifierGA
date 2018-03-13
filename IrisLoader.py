from sklearn.datasets import load_iris as ld


def load_iris():
    new_train_set = []
    iris = ld()
    # Arreglos de numpy
    train_data = iris.data
    train_labels = iris.target

    for item in train_data:
        new_train_set.append(item)

    return (new_train_set, train_labels)

from LinearModel import *


def calculate_fitness(id, problem, individual, training_set, labels):
    # Accuracy
    acc = 0
    # Loss
    L = 0

    N = len(training_set)

    for i in range(0, N):
        classification = linear_model(training_set[i], individual.phenotype)

        label = np.argmax(classification)
        L_i = calculate_loss(labels[i], classification, 1)
        L += L_i
        if label == labels[i]:
            acc += 1

    L = L / N
    L = np.asscalar(L)
    accuracy = acc / N

    print("Individual id: ", id, " | Accuracy: ", accuracy,
          " | Hinge Loss: ", L)
    return id, L, (acc / N)

import numpy as np


def linear_model(x, W):
    # Append 1 to the sample
    k = np.append(x, 1)
    k = np.reshape(k, (k.size, 1))

    # Linear Function
    return np.matmul(W, k)


def calculate_loss(y_i, m, delta):
    loss = 0
    for i in range(0, m.size):
        if i == y_i:
            pass
        else:
            loss += max(0, m[i] - m[y_i] + delta)
    return loss

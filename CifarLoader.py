import cv2
import numpy as np



def load_gray_Cifar():
    return train()

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


def load_test_set():
    #Test batch is loaded
    batch_t = unpickle("data/test_batch")[b'data']
    labels_t = unpickle("data/test_batch")[b'labels']

    #Test_set loaded as a numpy array
    test_set = np.array(batch_t)

    return (test_set, labels_t)


def load_training_set():
    #Each of the five batches is loaded
    batch_1 = unpickle("data/data_batch_1")[b'data']
    batch_2 = unpickle("data/data_batch_2")[b'data']
    batch_3 = unpickle("data/data_batch_3")[b'data']
    batch_4 = unpickle("data/data_batch_4")[b'data']
    batch_5 = unpickle("data/data_batch_5")[b'data']

    labels_1 = unpickle("data/data_batch_1")[b'labels']
    labels_2 = unpickle("data/data_batch_2")[b'labels']
    labels_3 = unpickle("data/data_batch_3")[b'labels']
    labels_4 = unpickle("data/data_batch_4")[b'labels']
    labels_5 = unpickle("data/data_batch_5")[b'labels']

    #training_set loaded as a vertical stack of all the batches
    training_set = np.vstack((batch_1, batch_2, batch_3, batch_4, batch_5))

    #labels loaded as a single list of length 50k
    labels = labels_1 + labels_2 + labels_3 + labels_4 + labels_5

    return(training_set, labels)


def train():
    #Load the global variables with data("Train" the model)
    (data,labels) = load_training_set()

    new_labels = []
    new_training_set = []

    for i in range(0,50000):
        label = labels[i]

        #Get only 4 classes for the test
        if label == 6 or label == 2 or label == 8 or label == 9:

            #label = 0 -> Bird
            #label = 1 -> Frog
            #label = 2 -> Ship
            #label = 3 -> Truck

            if label == 2:
                label = 0
            if label == 6:
                label = 1
            if label==8:
                label = 2
            if label==9:
                label = 3

            image = np.reshape(data[i, 0:3072], (3,32,32))
            #image = np.matrix.transpose(image)
            #image = np.rot90(image, k = 3)
            image = cv2.merge(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
            image = np.reshape(image,(1024,1))
            new_training_set.append(image)
            new_labels.append(label)

    return (new_training_set, new_labels)
train()



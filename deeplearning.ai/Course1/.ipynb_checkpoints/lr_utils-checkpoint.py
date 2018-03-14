import numpy as np
import h5py

def load_dataset():
    train_dataset = h5py.File('data/train_catvnoncat.h5','r')
    trainX = np.array(train_dataset["train_set_x"][:])
    trainY = np.array(train_dataset["train_set_y"][:])
    
    test_dataset = h5py.File('data/test_catvnoncat.h5','r')
    testX = np.array(test_dataset["test_set_x"][:])
    testY = np.array(test_dataset["test_set_y"][:])
    
    classes = np.array(test_dataset["list_classes"][:])
    
    trainY = trainY.reshape((1, trainY.shape[0]))
    testY = testY.reshape((1, testY.shape[0]))
    
    return trainX, trainY, testX, testY, classes
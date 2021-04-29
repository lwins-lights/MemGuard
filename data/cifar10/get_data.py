from keras.datasets import cifar10
import random
import numpy as np

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
np.savez('data_complete.npz', x=x_train, y=y_train)

#i = list(range(0, 50000))
#random.shuffle(i)
#np.savez('shuffle_index.npz', x=i)

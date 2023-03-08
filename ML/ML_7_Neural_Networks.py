# Gradient Descent Algorithm

# Loss function

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Already know the classifications of all the digits
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,ytest) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))
model.add(tf.keras.Dense(units=10,activation=tf.nn.softmax))

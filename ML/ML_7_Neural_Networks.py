# Gradient Descent Algorithm

# Loss function

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Already know the classifications of all the digits
# loading in data - already know classifications
mnist = tf.keras.datasets.mnist # mnist - handwritten digits dataset

# split into training, and testing data
(x_train,y_train),(x_test,y_test) = mnist.load_data()

# scaling down data (normalization) - y data = labels - dont want to scale
x_train = tf.keras.utils.normalize(x_train,axis=1)
x_test = tf.keras.utils.normalize(x_test,axis=1)

# Define the model

# Take an input layer  
model = tf.keras.models.Sequential() # create a feedforward NN
# Adding a new layer
model.add(tf.keras.layers.Flatten(input_shape=(28,28))) # 1D layer 28x28=pixels of image
# Dense Layer -  1st hidden layer
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu)) # all neurons are connected to prev and next layer
# units = neurons - more = more sophisticated - activation = rectify linear unit

# 2nd hidden layer
model.add(tf.keras.layers.Dense(units = 128, activation = tf.nn.relu))

# Output layer
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.softmax)) # softmax activation function
# softmax scales values down to - returns result probabilities


# Compilation - 
model.compile(optimizer = 'adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_train,y_train,epochs=3)
# epochs = how many times will the data be seen over again

accuracy, loss = model.evaluate(x_test,y_test)
print(accuracy)
print(loss)

model.save('digits.model')

for x in range(1,4):
    img = cv.imread(f'{x}.png')[:,:,0]
    img = np.invert(np.array([img])) # invert changes to black on white digits
    prediction = model.predict(img)
    print(f' The result is probably: {np.argmax(prediction)}')
    plt.imshow(img[0],cmap = plt.cm.binary)
    plt.show()


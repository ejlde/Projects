# MEAN SQUARED ERROR

# Linear Regression Model

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


time_studied = np.array([20,50,32,65,23,43,10,5,22,35,29,5,56]).reshape(-1,1)
scores = np.array([56,83,47,93,47,82,45,23,55,67,57,4,89]).reshape(-1,1)
# reshape(-1,1) = transpose

##
# Creating model
# model = LinearRegression()

# ##
# # Training model
# model.fit(time_studied,scores)

# ##
# # Predicting Model Output (score)
# print(model.predict(np.array([56]).reshape(-1,1)))
# ## 
# # Plotting Model
# plt.scatter(time_studied,scores)
# plt.plot(np.linspace(0,70,100).reshape(-1,1),model.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
# plt.ylim(0,100)
# plt.show()

##
# Testing

# Train test split
time_train, time_test, score_train, score_test = train_test_split(time_studied,scores,test_size = 0.3)
# test_size = % of data to be used to test model

model = LinearRegression()
model.fit(time_train,score_train)
print(model.score(time_test, score_test))

plt.scatter(time_train, score_train)
plt.plot(np.linspace(0,70,100).reshape(-1,1),model.predict(np.linspace(0,70,100).reshape(-1,1)),'r')
plt.show()


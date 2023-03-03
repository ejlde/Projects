# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:48:31 2023

@author: ejlde
"""

import numpy as np
#hi

x = np.array([
    [1,2,3,7],
    [4,5,6,7],
    [7,8,9,7]
    
    ])

#print(np.sin(x)) #np.exp()
# np.sum(x)
# np.max() -- np.min()
# np.mean()
# np.median()
# np.std()
#print(x.mean)

## 
# Shape Manipulation

x = x.reshape((2,6)) # 2x6 
#print(x)

#print(x.flatten()) # 1xwhatever the length is
#print(x.transpose())

#for a in x.flat:
#    print(a)
#print(a.flat[7])

##
# Joining arrays
a = np.array([
[1,2,3,7],
[4,5,6,7],
[7,8,9,7]
])

b = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [70,80,10,20],
])

c = np.concatenate((a,b)) # creates 6,4

c2 = np.stack((a,b)) # creates 2,3,4

#print(c)
#print(c2)

c3 = np.hstack((a,b)) # np.vstack()
#print(c3)

##
# Split Arrays

a = np.array([
[1,2,3,7],
[4,5,6,7],
[7,8,9,7],
[8,5,3,1]
])

print(np.split(a,4)) # needs to be an equal division
#np.hsplit()

##
# Adding Values
b = [10,20,30,40]




# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:17:57 2023

@author: ejlde
"""

import numpy as np
#import matplotlib
#tensorflow -- sklearn ##### laterrr

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

c = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])
print(c.shape)


##
# Fill arrays

a = np.zeros((5,7,3)) # np.ones #
# np.full((5,7,3),9)
# np.empty((5,7,3)) #non initalized 7x3 mats -- 5 of them
# np.random.random()
print(a)

##
# Range Functions

x = np.array([0,5,10,15,20,25,30])
y = x*2 - x**2 # ** = exponent

print(y)


x = np.arange(0,1000,5) # 5 = step size
y = np.sin(x)

#
x = np.linspace(0,1000,10) # 10 = num of elements


##
# Attributes
x = np.array([
    [
    [1,2,3],
    [4,5,6]
    ],[
       
    [10,20,30],
    [40,50,60],
      ] 
       ],dtype=float)
       
print(x.shape)
print(x.size)
print(x.ndim)
print(x.dtype)

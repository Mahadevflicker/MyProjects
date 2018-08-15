# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 14:59:49 2018

@author: appu
"""
#Importing Libraries
import matplotlib.pyplot as plt
import numpy as np
import random as random
#Declaring Array
x = np.arange(1, 10)

#Random variable
m = 1.2
c = -2

#Equation for straight line
y = m * x + c

#Random number Generations till 10
nums_one = [random.randrange(1,10) for p in range(1,50)]
nums_two = [random.randrange(1,10) for p in range(1,50)]

#Plotting the graph
plt.plot(x, y)
plt.plot(nums_one, nums_two, 'bo')

nums_zip = list(zip(nums_one,nums_two))

print(nums_one_zip)


y = np.array([-1,-1,1,1,1])

def perceptron_sgd(X, Y):
    w = np.zeros(len(X[0]))
    eta = 1
    epochs = 20

    for t in range(epochs):
        for i, x in enumerate(X):
            if (np.dot(X[i], w)*Y[i]) <= 0:
                w = w + eta*X[i]*Y[i]

    return w

w = perceptron_sgd(X,y)
print(w)

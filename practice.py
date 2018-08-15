# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 18:10:34 2018

@author: appu
"""
import math as m

a = 3
b = 4
c = 5
s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))
area = m.sqrt(area)
print(area)

a = [1,2,3,4,5,6,7,8,9,10]
asum = sum(a[0::2]) - sum(a[1::2])
print(asum)

import numpy as np
x = np.array([2,3,1,0])
x = np.zeros((2,3))


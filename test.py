# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 16:19:02 2018

@author: appu
"""

fin_lis = []
with open("Data.cus", 'r') as f:
    for line in f:
        lis = line.split(" ")
        fin_lis.append(lis[0])

print(fin_lis[len(fin_lis)-1])
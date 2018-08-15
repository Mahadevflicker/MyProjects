# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:25:52 2018

@author: appu
"""

import datetime 
import os
timeNow = datetime.datetime.now()
year = datetime.date.today().strftime("%Y")
month = datetime.date.today().strftime("%m")
dirMonth =int(str(year) + str(month))
dirMonth = str(dirMonth)
print ("Day of the month : ", dirMonth)

if not (os.path.isdir(dirM0onth)):
    os.mkdir(dirMonth)

print("Please enter the directory")
ChangeTask = input()

if not os.path.exists(os.path.join(dirMonth, ChangeTask)):
    os.makedirs(os.path.join(dirMonth, ChangeTask))


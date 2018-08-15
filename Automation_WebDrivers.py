# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:37:19 2018

@author: appu
"""

from selenium import webdriver

def _list(name):
    name = dir(name)
    for i in range(len(name)):
        print(i+1,name[i])
        
_list(webdriver)

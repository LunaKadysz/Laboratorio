# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:36:39 2019

@author: Luna
"""
import random
import numpy as np
import matplotlib.pyplot as plt


 # ese array tiene 1000 elementos, andar printeando es poco práctico!
x = np.linspace(0, 5, 40)

def f(t):
    return 2* np.exp(-3*t)


list = ['yellow','green','blue','red']
ruido=[]
size=[]
color=[]
# creating a noise with the same dimension as the dataset (2,2) 
for i in np.nditer(f(x)):
    size.append(np.random.normal(0,10,1)**2)
    ruido.append(np.random.normal(0, 3,1)**2)
    color.append(random.choice(list))
 
plt.scatter(x, ruido, s=size,alpha = 0.8, c = color)
plt.axis([0, 6, -20, 26])

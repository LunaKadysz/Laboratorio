# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 19:33:13 2019

@author: Luna
"""
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('temp-tiemp.txt', delimiter = ',' )

np.transpose(data)
tiempo = np.array(data[:,0])
temp = np.array(data[:,1])


plt.title('Funcion')
plt.xlabel('Tiempo [s]')
plt.ylabel('Temperatura [C]')
plt.scatter(tiempo, temp) 
plt.show() 
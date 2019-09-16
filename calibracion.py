# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:50:34 2019

@author: Luna Kadysz
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('calibracion.txt', delimiter = '\t' )

np.transpose(data)
tiempo = np.array(data[:,0])
temp = np.array(data[:,1])


plt.title('Calibración')
plt.xlabel('Tiempo [s]')
plt.ylabel('Temperatura [C]')
plt.scatter(tiempo, temp) 
plt.show() 
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:10:55 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy

# C = 0.01microF
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V


dato = scipy.io.loadmat('RC.m')
matriz = np.array(dato['salida'])

tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

plt.figure()
plt.scatter(tiempo,Vc,s= 1)
plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
plt.show()

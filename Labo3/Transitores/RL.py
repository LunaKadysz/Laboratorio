# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:41:33 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy

# L = 1H
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V

dato = scipy.io.loadmat('RL.m')
matriz = np.array(dato['salida'])

tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

plt.figure()
plt.scatter(tiempo,Vc,s= 0.5)
plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
plt.xlim(-0.0018,0.005)
plt.show()

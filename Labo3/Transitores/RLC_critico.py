# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:03:12 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import scipy


# sobreamortiguado: R>2* np.sqrt(L/C) 60k de resist
# critico R = 2 * np.sqrt(L/C)  20k resist
# subamortiguado R<2* np.sqrt(L/C) 4k resist
# C = 1e-08F
# L = 1H
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V

dato = scipy.io.loadmat('RLC_critico.m')
matriz = np.array(dato['salida'])

tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

plt.figure()
plt.scatter(tiempo,Vc,s= 0.5)
plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
plt.show()
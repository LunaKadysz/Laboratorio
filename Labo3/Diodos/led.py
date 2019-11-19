# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:10:17 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data_rojo = np.loadtxt('led.txt')
matriz_rojo = np.array(data_rojo)

tiempo_rojo = matriz_rojo[:,0]
V1_rojo = matriz_rojo[:,1]
V2_rojo = matriz_rojo[:,2]


plt.scatter(V1_rojo,V2_rojo)
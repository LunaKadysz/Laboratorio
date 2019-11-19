# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:23:01 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data_verde = np.loadtxt('ledVerde.txt')
matriz_verde = np.array(data_verde)

tiempo_verde = matriz_verde[:,0]
V1_verde = matriz_verde[:,1]
V2_verde = matriz_verde[:,2]

plt.scatter(V1_verde,V2_verde)
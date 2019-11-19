# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:59:00 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


data_diodo = np.loadtxt('diodo.txt')
matriz_diodo = np.array(data_diodo)

tiempo_diodo = matriz_diodo[:,0]
V1_diodo = matriz_diodo[:,1]
V2_diodo = matriz_diodo[:,2]

plt.scatter(V1_diodo,V2_diodo)


data_zener = np.loadtxt('zener.txt')
matriz_zener = np.array(data_zener)

tiempo_zener = matriz_zener[:,0]
V1_zener = matriz_zener[:,1]
V2_zener = matriz_zener[:,2]

plt.scatter(V1_zener,V2_zener)


data_rojo = np.loadtxt('led.txt')
matriz_rojo = np.array(data_rojo)

tiempo_rojo = matriz_rojo[:,0]
V1_rojo = matriz_rojo[:,1]
V2_rojo = matriz_rojo[:,2]

plt.scatter(V1_rojo,V2_rojo)


data_verde = np.loadtxt('ledVerde.txt')
matriz_verde = np.array(data_verde)

tiempo_verde = matriz_verde[:,0]
V1_verde = matriz_verde[:,1]
V2_verde = matriz_verde[:,2]

plt.scatter(V1_verde,V2_verde)

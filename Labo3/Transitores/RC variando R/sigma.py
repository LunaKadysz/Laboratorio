# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:29:32 2019

@author: Luna Kadysz
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics 


# C = 0.01microF
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V


data = np.loadtxt('R4k.txt')
matriz = np.array(data)

tiempo = matriz[:,0]
Vc = matriz[:,1]
t = tiempo[1200:2240]
V = Vc[1200:2240]
    
plt.scatter(t,V,s= 0.1,color = "red")

std = statistics.stdev(V)
sigma = np.sqrt(std**2 + 0.005**2)

print("Standard Deviation is % s " 
                % (statistics.stdev(V))) 

print("Sigma is % s " 
                % sigma) 
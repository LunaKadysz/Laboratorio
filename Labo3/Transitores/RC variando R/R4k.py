# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:12:41 2019

@author: Publico
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# C = 0.01microF
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V


data = np.loadtxt('R4k.txt')
matriz = np.array(data)

tiempo = matriz[:,0]
Vc = matriz[:,1]
t = tiempo[160:2241]
V = Vc[160:2241] + 2.47
    
def f(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param, param_cov = curve_fit(f,t,V, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion

plt.figure()
plt.plot(t,f(t,param[0],param[1],param[2]))
plt.scatter(t,V,s= 0.1,color = "red")
plt.show()


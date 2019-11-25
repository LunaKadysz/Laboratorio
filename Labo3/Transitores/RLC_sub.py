# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:33:08 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy import io
import scipy


# sobreamortiguado: R>2* np.sqrt(L/C) 60k de resist
# critico R = 2 * np.sqrt(L/C)  20k resist
# subamortiguado R<2* np.sqrt(L/C) 4k resist
# C = 1e-08F
# L = 1H
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V

x = np.linspace(0,10,1000)
A = 1.5
R = 4000
L = 10000

dato = scipy.io.loadmat('RLC_sub.m')
matriz = np.array(dato['salida'])

xmax = [0.00680103,0.00744242,0.00811029,0.00869158]
ymax = [1.52125,0.401549,0.163974,0.0834046]


tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

def Tiempo(t):
    return t[420:950]
    
def V(Vc):
    return Vc[420:950]

def f(t,V0,tau):
    return V0 * np.e**(-t/tau)

err = []
for i in range(530):
    a = np.random.normal(0.005, 0.01)
    err.append(a)

param, param_cov = curve_fit(f,xmax,ymax, p0=[1.52,2/4000]) 

plt.figure()
plt.plot(Tiempo(tiempo)*1000,f(Tiempo(tiempo),param[0],param[1]), '--', color ='blue', label ="Ajuste") 
#plt.scatter(Tiempo(tiempo),V(Vc),s= 5,color = "blue",alpha=0.4, label ="Datos")
plt.errorbar(Tiempo(tiempo)*1000,V(Vc),yerr=err, fmt='.',color ='black',label ="Datos", ecolor = 'red')

#plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
#plt.ylim(0,5)
plt.title('Transitor Subamortiguado')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Corriente [A] ')
plt.legend()
plt.show()

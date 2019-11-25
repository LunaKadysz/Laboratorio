# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:03:12 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
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



dato = scipy.io.loadmat('RLC_critico.m')
matriz = np.array(dato['salida'])

tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

def Tiempo(t):
    return t[445:900]
    
def V(Vc):
    return Vc[445:900]

def f(t,V0,tau):
    return V0  * np.e**(-t/tau) 


param, param_cov = curve_fit(f,Tiempo(tiempo),V(Vc), p0=[2,.00025]) 


plt.figure()
plt.plot(Tiempo(tiempo)*1000,f(Tiempo(tiempo),param[0],param[1]), '--', color ='red', label ="Ajuste") 
plt.scatter(Tiempo(tiempo)*1000,V(Vc),s= 5,color = "blue",alpha=0.4, label ="Datos")

#plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
#plt.ylim(0,5)
plt.title('Transitor RLC Critico')
plt.xlabel('Tiempo [ms]')
plt.ylabel('Corriente [A] ')
plt.legend()
plt.show()

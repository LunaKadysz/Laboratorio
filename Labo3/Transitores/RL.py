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
# frec = 300Hz => periodo = 0.00333333333shttps://towardsdatascience.com/playing-with-time-series-data-in-python-959e2485bff8
# Vpicopico = 5V con offset de 2.5V

dato = scipy.io.loadmat('RL.m')
matriz = np.array(dato['salida'])

tiempo = matriz[:,0]
Vc = matriz[:,1]
Vfuente = matriz[:,2]

def Tiempo(t):
    return t[422:900]
    
def V(Vc):
    return Vc[422:900]

def f(t,V0,tau):
    return V0 * np.e**(-t/tau)

param, param_cov = curve_fit(f,Tiempo(tiempo),V(Vc), p0=[5,0.00025]) 


plt.figure()
plt.plot(Tiempo(tiempo),f(Tiempo(tiempo),param[0],param[1]), '--', color ='red', label ="Ajuste") 
plt.scatter(Tiempo(tiempo),V(Vc),s= 5,color = "blue",alpha=0.4, label ="Datos")
#plt.scatter(tiempo,Vfuente,color='orange',s= 0.5)
#plt.ylim(0,5)
plt.title('Transitor RL')
plt.xlabel('Tiempo [s]')
plt.ylabel('Corriente [A] ')
plt.legend()
plt.show()


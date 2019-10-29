# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:56:22 2019

@author: Publico
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 #frec = 1kHz
N1 = 2920
N2 = 235

V1 = np.array([2.93,3.9,4.9,5.82,6.76,7.7,8.64,9.64])
err_V1 = np.array([0.01,0.02,0.02,0.02,0.04,0.02,0.005,0.04])
V2 = np.array([0.15,0.2,0.23,0.25,0.295,0.32,0.368,0.395])
err_V2 = np.array([0.04,0.03,0.03,0.02,0.03,0.02,0.03,0.03])

def f(V1,k):
    return k*V1*0.08
    
param, param_cov = curve_fit(f,V1,V2, p0=[0.5]) 

plt.errorbar(V1,V2,yerr=err_V2, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(V1, f(V1,param[0]), '--', color ='blue', label ="Ajuste") 
plt.scatter()


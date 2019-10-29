# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:37:15 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 #frec = 1kHz
N1 = 400
N2 = 200


V1 = np.array([3.1,4.1,5.1,6.1,7.1,8.1,9.1,10])
err_V1 = np.array([0.04,0.04,0.04,0.04,0.04,0.04,0.04,0.005])
V2 = np.array([0.5,0.64,0.81,0.98,1.12,1.28,1.45,1.66])
err_V2 = np.array([0.03,0.03,0.03,0.03,0.02,0.03,0.03,0.02])

def f(V1,k):
    return k*V1/2
    
param, param_cov = curve_fit(f,V1,V2, p0=[0.5]) 

plt.errorbar(V1,V2,yerr=err_V2, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(V1, f(V1,param[0]), '--', color ='blue', label ="Ajuste") 
plt.scatter()

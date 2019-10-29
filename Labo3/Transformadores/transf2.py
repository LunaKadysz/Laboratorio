# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:16:29 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 #frec = 1kHz
N1 = 400
N2 = 1600


V1 = np.array([2.9,3.9,4.80,5.78,6.68,7.56,8.52,9.48])
err_V1 = np.array([0.02,0.04,0.04,0.04,0.06,0.04,0.04,0.04])
V2 = np.array([7.04,9.4,11.6,14,16.7,19.2,21.6,24])
err_V2 = np.array([0.04,0.04,0.1,0.05,0.1,0.05,0.05,0.2])

def f(V1,k):
    return k*V1*4
    
param, param_cov = curve_fit(f,V1,V2, p0=[0.5]) 

plt.errorbar(V1,V2,yerr=err_V2, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(V1, f(V1,param[0]), '--', color ='blue', label ="Ajuste") 
plt.scatter()


# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 15:49:11 2019

@author: Publico
"""

              ### Thèvenin ###
              
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#escala amperimetro: 2m

Vo = 5 #[V]


Rc = np.array([600, 999, 1599, 1990, 2600, 3000, 3590, 3990, 5000, 5990])
Ic = np.array([1.357, 1.225, 1.069, 0.985, 0.881, 0.823, 0.75, 0.708, 0.620, 0.552])

err_Rc = np.array([0.5,0.5,0.5,5,5,5,5,5,5,5])
err_Ic = np.array([0.0005, 0.001, 0.0005, 0.0005, 0.001, 0.001, 0.0005, 0.0005, 0.001, 0.0005])

Vc = Rc * Ic
A = (Rc*err_Ic)**2
B = (Ic*err_Rc)**2
err_Vc = np.sqrt(A + B)

def lineal (x, m, b):
    return m*x+b

param, param_cov = curve_fit(lineal, Ic, Vc) 
  
print("Resistencia Thévenin:") 
print(-param[0]) 
print("Pila Equivalente Thèvenin:") 
print(param[1]) 
print("Covariance of coefficients:") 
print(param_cov) 

ans2 = (param[0]* Ic + param[1]) 

plt.plot(Ic, ans2, '--', color ='blue', label ="Ajuste Lineal") 
plt.errorbar(Ic, Vc, yerr=err_Vc, fmt='.',color ='red')
plt.legend() 
plt.show() 
    



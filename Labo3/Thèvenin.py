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


Rc = [600, 999, 1599, 1990, 2600, 3000, 3590, 3990, 5000, 5990]
Ic = [1.357, 1.225, 1.069, 0.985, 0.881, 0.823, 0.75, 0.708, 0.620, 0.552]
Vc = []

err_Rc = [0.5,0.5,0.5,5,5,5,5,5,5,5]
err_Ic = [0.0005, 0.001, 0.0005, 0.0005, 0.001, 0.001, 0.0005, 0.0005, 0.001, 0.0005]
err_Vc = []


for i in range(len(Rc)):
    Vc.append(Rc[i]*Ic[i])
    
    A = (Rc[i]*err_Ic[i])**2
    B = (Ic[i]*err_Rc[i])**2
    ΔVc = np.sqrt(A+B)
    err_Vc.append(ΔVc)

RC = np.array(Rc)
IC = np.array(Ic)
VC = np.array(Vc)
err_VC = np.array(err_Vc)
    
def lineal (x, m, b):
    return m*x+b

param, param_cov = curve_fit(lineal, IC, VC) 
  
print("Resistencia Thévenin:") 
print(-param[0]) 
print("Pila Equivalente Thèvenin:") 
print(param[1]) 
print("Covariance of coefficients:") 
print(param_cov) 

ans2 = (param[0]* IC + param[1]) 

plt.plot(IC, ans2, '--', color ='blue', label ="Ajuste Lineal") 
plt.errorbar(IC, VC, yerr=err_VC, fmt='.',color ='red')
plt.legend() 
plt.show() 
    



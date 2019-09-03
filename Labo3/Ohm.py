# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 14:24:19 2019

@author: Publico
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 
                         ##### Ohm #####

 # [I] = 2mA ; [R] = Ohm ; QUE ESCALA USAMOS??
 
R = 4734 
fuente = np.array([2,3,4,5,6,7,8,9,10,11,12,13,14])
voltimetro = np.array([1.962,2.953,3.93,4.92,5.91,6.87,7.84,8.82,10,11.01,12.01,13.02,13.28])
I = np.array([0.406,0.611,0.83,1.019,1.223,1.422,1.623,1.826,2.07,2.28,2.49,2.7,2.9])

error_fuente = np.array([0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005])
error_voltimetro = np.array([0.001,0.001,0.005,0.005,0.005,0.005,0.01,0.01,0.05,0.01,0.005,0.01,0.005])
error_I = np.array([0.0005,0.0005,0.0005,0.001,0.0005,0.0005,0.001,0.0005,0.005,0.005,0.005,0.005,0.005])

plt.figure()
plt.scatter(I, voltimetro)


  
def f(I, m, b): 
    return I*m+b
  
param, param_cov = curve_fit(f, I, voltimetro) 
  
print("Resistencia:") 
print(param[0]) 
print("Ordenada al origen:") 
print(param[1]) 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = (param[0]* I + param[1]) 
  
plt.plot(I, voltimetro, 'o', color ='red', label ="Datos") 
plt.plot(I, ans, '--', color ='blue', label ="Ajuste Lineal") 
plt.legend() 
plt.show() 
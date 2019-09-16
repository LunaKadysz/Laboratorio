# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 08:50:40 2019

@author: Luna Kadysz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit 

data = np.loadtxt('rata.txt', delimiter = '\t' )

np.transpose(data)
tiempo = np.array(data[:,0])
temp = np.array(data[:,1])


def f(t, m, b): 
    return t*m+b
  
param, param_cov = curve_fit(f, tiempo, temp) 
  
print("Pendiente:") 
print(param[0]) 
print("Ordenada al origen:") 
print(param[1]) 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = (param[0]* tiempo + param[1]) 
  
plt.plot(tiempo, temp, 'o', color ='red', label ="Datos") 
plt.plot(tiempo, ans1, '--', color ='blue', label ="Ajuste Lineal") 
plt.title('Calorimetro con muestra de rata')
plt.xlabel('Tiempo [s]')
plt.ylabel('Temperatura [C]')
plt.legend() 
plt.show() 
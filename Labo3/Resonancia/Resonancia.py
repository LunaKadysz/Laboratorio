# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:45:00 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#L = 1 [Henrio]
#C = 1 [muFaradio]

#w0 = 2*np.pi*f0 = 1/np.sqrt(L*C)

#f0 = 159.15 +- err [Hz]

R = np.array([5000, 500, 50]) # Ra; Rb; Rc
x = np.linspace(10,3000,10)
#frecuencias_a = np.array([50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,350])
#err_frec_a = np.array([0.05, 0.1, 0.2,0.2,0.2,0.2,0.1,0.05,0.2,0.05,0.1,0.1,0.1,0.2,0.2,0.1,0.1,0.05,0.2,0.2,0.2,0.2,0.2,0.1])

#V_a = np.array([42.4,44.2, 45.6, 46.4,46.8,47.2,47.4,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,48.0,47.8,47.6,47.2,47.2,47.2,46.2])
#err_Va = np.array([0.05, 0.1, 0.05, 0.05, 0.05,0.05,0.2,0.2,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.05,0.05,0.05,0.05,0.05])

frec_a = np.array([10,20,30,50,100,150,160,200,250,300,350,400,500,600,800,1000,1500,2000,3000])
err_frec_a = np.array([0.02,0.1,0.02,0.1,0.1,0.05,0.2,0.2,0.2,0.2,0.2,0.2,0.05,0.1,1,1,3,4,2])

V_a = np.array([15.6,27.2,34.8,42.0,47.2,48.0,48.0,48.2,47.6,47.0,46.4,45.2,43.2,40.8,36.6,32.4,24.8,19.6,13.6])
err_Va = np.array([0.05,0.01,0.05,0.05,0.05,0.05,0.05,0.1,0.2,0.2,0.2,0.05,0.2,0.05,0.2,0.05,0.05,0.2,0.05])

frec_b = np.array([20,40,60,80,100,120,140,160,180,200,300,400,500,600,800,1000,1500])
err_frec_b = np.array([0.02,0.05,0.05,0.1,0.1,0.1,0.1,0.3,0.1,0.4,0.4,0.2,0.5,0.5,1,2,3])

V_b = np.array([3.8,7.2,11.2,15.2,20.2,25.2,29.2,30,29.2,26.8,16.4,11.8,9.2,7.6,5.6,4.6,3.2])
err_V_b = np.array([0.2,0.05,0.05,0.05,0.05,0.2,0.2,0.2,0.05,0.2,0.05,0.2,0.05,0.05,0.05,0.02,0.05])

frec_c = np.array([20,40,60,80,100,120,140,160,180,200,300,400,500,1000,1500])
err_frec_c = np.array([0.05,0.1,0.1,0.02,0.2,0.5,0.2,0.2,0.2,0.1,0.2,0.2,0.5,0.5,1])

V_c = np.array([1,1.2,1.8,2.4,3,4.2,5.8,6.6,5.8,4.6,2.4,2,1.6,1.2,0.6])
err_V_c = np.array([0.2,0.05,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.05,0.05,0.05,0.05,0.2])




x = np.linspace(0,3000,1000)

#def f(frec,R,C):
 #   return np.sqrt((frec*R)**2)/(np.sqrt(R**2+(frec - 1/(frec*C))**2))
def f(frec,f0,E,A0,T0):
    w = 2*np.pi*frec
    w0 = 2*np.pi*f0
    A = (w/w0)-(w0/w)
    B = 2*E
    C = (B/A)**2
    return (A0/np.sqrt(1+C))+T0


param_a, param_cov_a = curve_fit(f,frec_a,V_a/R[0], p0=[159,0.1,0.6,0.3]) 
  
print("Covariance of coefficients:") 
print(param_cov_a) 
print(param_a[0])
print(param_a[1])

param_b, param_cov_b = curve_fit(f,frec_b,V_b/R[1], p0=[159,0.1,0.6,0.3]) 
  
print("Covariance of coefficients:") 
print(param_cov_b) 
print(param_b[0])
print(param_b[1])

param_c, param_cov_c = curve_fit(f,frec_c,V_c/R[2], p0=[159,0.1,0.6,0.3]) 
  
print("Covariance of coefficients:") 
print(param_cov_c) 
print(param_b[0])
print(param_b[1])





plt.figure()
plt.plot(x,f(x,param_a[0],param_a[1],param_a[2],param_a[3]), '--', label ="Ajuste") 
plt.plot(x,f(x,param_b[0],param_b[1],param_b[2],param_b[3]), '--', color ='green', label ="Ajuste") 
plt.plot(x,f(x,param_c[0],param_c[1],param_c[2],param_c[3]), '--', color ='orange', label ="Ajuste") 
plt.title("Curvas de I(f) para distintos valores de resistencia")
plt.scatter(frec_a,V_a/(R[0]), s= 15, label ="Datos")
plt.scatter(frec_b, V_b/R[1], color = 'green',s=15, label ="Datos")
plt.scatter(frec_c , V_c/R[2], color = 'orange',s=15, label ="Datos")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Corriente [A]")
plt.legend()
plt.show()








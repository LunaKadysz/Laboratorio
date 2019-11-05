# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:18:48 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data10 = np.loadtxt('R10k.txt')
matriz10 = np.array(data10)

tiempo10 = matriz10[:,0]
Vc10 = matriz10[:,1]
t10 = tiempo10[160:2241]
V10 = Vc10[160:2241] + 2.47
    
def f10(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param10, param_cov10 = curve_fit(f10,t10,V10, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion


plt.plot(t10,f10(t10,param10[0],param10[1],param10[2]))
plt.scatter(t10,V10,s= 0.1,color = "red")


data4 = np.loadtxt('R4k.txt')
matriz4 = np.array(data4)

tiempo4 = matriz4[:,0]
Vc4 = matriz4[:,1]
t4 = tiempo4[160:2241]
V4 = Vc4[160:2241] + 2.47
    
def f4(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param4, param_cov4 = curve_fit(f4,t4,V4, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion


plt.plot(t4,f4(t4,param4[0],param4[1],param4[2]))
plt.scatter(t4,V4,s= 0.1,color = "orange")

data6 = np.loadtxt('R6k.txt')
matriz6 = np.array(data6)

tiempo6 = matriz6[:,0]
Vc6 = matriz6[:,1]
t6 = tiempo6[160:2241]
V6 = Vc6[160:2241] + 2.47
    
def f6(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param6, param_cov6 = curve_fit(f6,t6,V6, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion

plt.plot(t6,f6(t6,param6[0],param6[1],param6[2]))
plt.scatter(t6,V6,s= 0.1,color = "red")

data = np.loadtxt('R8k.txt')
matriz = np.array(data)

tiempo = matriz[:,0]
Vc = matriz[:,1]
t = tiempo[160:2241]
V = Vc[160:2241] + 2.47
    
def f(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param, param_cov = curve_fit(f,t,V, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion


plt.plot(t,f(t,param[0],param[1],param[2]))
plt.scatter(t,V,s= 0.1,color = "red")
plt.show()
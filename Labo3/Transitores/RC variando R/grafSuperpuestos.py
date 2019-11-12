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

# errores

err1 = []
for i in range(2081):
    a = np.random.normal(0.005, 0.01)
    err1.append(a)
    
err2 = []
for i in range(2081):
    a = np.random.normal(0.005, 0.01)
    err2.append(a)
    
err3 = []
for i in range(2081):
    a = np.random.normal(0.005, 0.01)
    err3.append(a)

err4 = []
for i in range(2081):
    a = np.random.normal(0.005, 0.01)
    err4.append(a)

######
    
def f10(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param10, param_cov10 = curve_fit(f10,t10,V10, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion


plt.plot(t10,f10(t10,param10[0],param10[1],param10[2]), '--',lw = 2,color = "yellow",label = "Ajuste R = 6k Ohms")
#plt.scatter(t10,V10,s= 0.1,color = "red")
plt.errorbar(t10,V10,yerr=err1, fmt=':',color ='black', ecolor = 'red')

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


plt.plot(t4,f4(t4,param4[0],param4[1],param4[2]),  '--',lw = 2,color = "blue",label = "Ajuste R = 4k Ohms")
plt.errorbar(t4,V4,yerr=err4, fmt=':',color ='black', ecolor = 'red')

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

plt.plot(t6,f6(t6,param6[0],param6[1],param6[2]),  '--',lw = 2,color = "green",label = "Ajuste R = 6k Ohms")
plt.errorbar(t6,V6,yerr=err3, fmt=':',color ='black',ecolor = "red",label ="Datos")

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


plt.plot(t,f(t,param[0],param[1],param[2]),  '--',color = "red",lw = 2,label = "Ajuste R = 8k Ohms")
plt.errorbar(t,V,yerr=err2, fmt=':',color ='black', ecolor = 'red')
plt.title("RC variando valor de R")
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V] ')
plt.legend()
plt.show()
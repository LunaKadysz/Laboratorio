# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 18:49:38 2019

@author: Publico
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# C = 0.01microF
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V


data = np.loadtxt('R10k.txt')
matriz = np.array(data)

tiempo = matriz[:,0]
Vc = matriz[:,1]
t = tiempo[160:2241]
V = Vc[160:2241] + 2.47
    
def f(t,V0,Vc0,tau):
    return Vc0 + (V0 - Vc0)*(1 - np.e**(-t/tau))

 #fitteo con la funcion
param, param_cov = curve_fit(f,t,V, p0=[5,0.07,0.01]) #p0 son los parametros de estimacion

plt.figure()
plt.plot(t,f(t,param[0],param[1],param[2]))
plt.scatter(t,V,s= 0.1,color = "red")
plt.show()


def chi_square(y_data, y_model, sigma):
    return np.sum((y_data/sigma - y_model/sigma)**2)

def r_chi_square(chi, y_data, dof):
    nu = len(y_data) - 1 - dof
    if nu < 1:
        raise ValueError('length of y_data - 1 - dof should be greater than 1')
    return chi / nu

def p_value(chi, y_data, dof):
    nu = len(y_data) - 1 - dof
    if nu < 1:
        raise ValueError('length of y_data - 1 - dof should be greater than 1')
    
    p = 1 - st.chi2.cdf(chi, nu)
    return p

fit = f(t,param[0],param[1],param[2])

#sigma = np.sqrt(param_cov[0,0])
sigma = 0.021294271318071607 

chi = chi_square(V,fit,sigma)
r = r_chi_square(chi, V, len(param))
p =  p_value(chi, V, len(param))

print(f'Chi square: {chi:.11f}')
print(f'r: {r:.11f}')
print(f'p: {p:.11f}')
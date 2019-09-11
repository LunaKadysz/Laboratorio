# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:32:15 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

Ri = 1000
Rc = np.array([0,100.200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,3000,4000,5000,6000,7000,8000,9000,10000])
Ic = np.array([4.96,4.53,4.15,3.84,3.57,3.33,3.13,2.94,2.78,2.64,2.5,2.38,2.28,2.18,2.09,2,1.93,1.85,1.79,1.73,1.25,1,0.84,0.72,0.63,0.56,0.5,0.45])



err_Ic = np.array(Rc*0.03)

def f(R,V,ri):
    return ((V/(ri+R))**2) * R 

  
param, param_cov = curve_fit(f,Rc ,(Ic**2) * Rc, p0=[5,0.5]) 
  
print("V:") 
print(param[0]) 
print("ri:") 
print(param[0]) 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = (((param[0]/(param[1]+Rc))**2) * Rc) 

plt.errorbar(Rc, (Ic**2) * Rc, yerr=err_Ic, fmt = "o", color ='green', label ="Datos") 
plt.plot(Rc, ans1, '-', color ='blue', label ="Ajuste") 
plt.title('Máxima Potencia')
plt.xlabel('Resistencia [Ohm]')
plt.ylabel('Potencia [P]')


#y = (Ic**2) * Rc
#xpos = y.argmax()
#xmax = Rc[xpos]

xmax = param[1]
ymax = f(xmax, *param)

plt.annotate(round(xmax, 2), xy=(xmax, ymax), xytext=(xmax, -460), ha='center', color='red')
plt.vlines(xmax, 0, ymax, linestyles= '--', color ='red')
plt.ylim(0,ymax*1.1)
plt.legend()
plt.show()


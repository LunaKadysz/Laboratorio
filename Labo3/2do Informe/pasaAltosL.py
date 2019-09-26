# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:51:20 2019

@author: Publico
"""

#[frec] = Hz f0 = 320hz +- err
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

frec = np.array([10,50,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,420,440,450,550,650,750,1000])
V_ent = np.array(len(frec)*[9.92])
V_sal = np.array([1.64,2.08,2.96,3.34,3.84,4.16,4.52,4.88,5.2,5.6,5.84,6.08,6.32,6.56,6.8,7.04,7.28,7.36,7.52,7.68,7.74,8.4,8.8,9.12,9.48])



err_Vent = np.array([0.005*len(frec)])
err_Vsal = np.array([0.005*len(frec)])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)

def f(frec,f0):
    return 1/(np.sqrt(1+(frec/f0)**(-2)))

  
param, param_cov = curve_fit(f,frec, V_sal/V_ent, p0=[159.15]) 
  
print("V:") 
print(param[0]) 
print("ri:") 
print(param[0]) 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = 1/(np.sqrt(1+(frec/param[0])**(-2)))

plt.errorbar(frec,V_sal/V_ent,yerr=propagacion, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(frec, ans1, '--', color ='blue', label ="Ajuste") 
plt.title('Pasa altos con Inductancia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia ')



xmax = param[0]
ymax = f(xmax, *param)


plt.ylim(0,ymax*1.5)
plt.legend(loc="best")
plt.show()

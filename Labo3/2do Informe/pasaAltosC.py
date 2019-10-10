# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 16:31:59 2019

@author: Publico
"""

#[frec] = Hz f0= 159.15 +- err
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

frec = np.array([10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,120,130,140,150,160,170,180,190,200,250,300,350,400,500,1000])*2*np.pi
V_ent = np.array(len(frec)*[10.4])
V_sal = np.array([0.72,1.04,1.32,1.64,2,2.28,2.56,2.84,3.12,3.4,3.68,3.88,4.16,4.4,4.56,4.8,5.04,5.28,5.44,5.6,5.76,6.08,6.4,6.64,6.88,7.12,7.28,7.44,7.60,7.76,8.32,8.7,8.88,9.04,9.28,9.6])



err_Vent = np.array([0.005*len(frec)])
err_Vsal = np.array([0.005*len(frec)])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)




def f(frec,f0):
    return 1/(np.sqrt(1+(frec/f0)**(-2)))

  
param, param_cov = curve_fit(f,frec,V_sal/V_ent, p0=[159.15]) 
  
print("V:") 
print(param[0]) 
print("ri:") 
print(param[0]) 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = 1/(np.sqrt(1+(frec/param[0])**(-2)))

plt.errorbar(frec,V_sal/V_ent,yerr=propagacion, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(frec, ans1, '--', color ='blue', label ="Ajuste") 
plt.title('Pasa altos con Capacitor')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia ')



xmax = param[0]
ymax = f(xmax, *param)


plt.ylim(0,ymax*1.5)
plt.legend(loc="best")
plt.show()


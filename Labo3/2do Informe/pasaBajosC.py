# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 19:14:15 2019

@author: Publico
"""
#[frec] = Hz f0=159,15 +- err
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

frec = np.array([10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,250,300,350,400,450,500,550,600,650,700,800,900,1000,1250,1500])
V_ent = np.array(len(frec)*[10.4])
V_sal = np.array([10.4,10.2,10.2,10,9.8,9.6,9.4,9.2,8.8,8.6,8.4,8,7.8,7.6,7.4,7.2,6.9,6.6,6.4,6.2,6,5.8,5.4,4.8,4.2,3.8,3.4,3,2.9,2.7,2.4,2.2,1.92,1.74,1.58,1.27,1.08])



err_Vent = np.array([0.01*len(frec)])
err_Vsal = np.array([0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)


def f(frec,f0):
    return 1/(np.sqrt(1+(frec/f0)**(2)))

  
param, param_cov = curve_fit(f,frec, V_sal/V_ent, p0=[159.15]) 
  
print("f0") 
print(param[0]) 
 
print("Covariance of coefficients:") 
print(param_cov) 
  
ans1 = f(frec,param[0])
plt.errorbar(frec,V_sal/V_ent,yerr=propagacion, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(frec, ans1, '--', color ='blue', label ="Ajuste") 
plt.title('Pasa bajos con Capacitor')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia ')



xmax = param[0]
ymax = f(xmax, *param)


plt.ylim(0,ymax*1.5)
plt.legend(loc="best")
plt.show()

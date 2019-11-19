# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:18:07 2019

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
x = np.linspace(10,400,10000)


#V = np.array([1,1.2,1.8,2.4,3,4.2,5.8,6.6,5.8,4.6,2.4,2,1.6,1.2,0.6])
#err_V = np.array([0.2,0.05,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.05,0.05,0.05,0.05,0.2])

    
def P(frec,f0,E,A0,T0):
    w = 2*np.pi*frec
    w0 = 2*np.pi*f0
    A = (w/w0)-(w0/w)
    B = 2*E
    C = (B/A)**2
    return 50*((A0/np.sqrt(1+C))+T0)**2



#param_a, param_cov_a = curve_fit(P,frec,P, p0=[159,0.1,0.6,0.3]) 
  


plt.figure()
#plt.plot(x,f(x,param_a[0],param_a[1],param_a[2],param_a[3]), '--', label ="Ajuste") 
plt.plot(x,P(x,158.8,0.62,-0.1,0.13),color="red")

plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Potencia[Watts]")
plt.legend()
plt.show()


y = P(x,158.8,0.62,-0.1,0.13)
ymax = max(y)

w1 = x[2906]
w2 = x[4985]


plt.hlines(ymax/2, 0,w2, linestyles= '--', color ='black')
plt.vlines(w1, 0,y[2906], linestyles= '--', color ='black')
plt.vlines(w2, 0,y[4985], linestyles= '--', color ='black')
plt.annotate(round(w1, 2), xy=(w1, ymax), xytext=(w1, 0), ha='center', color='red')
plt.annotate(round(w2, 2), xy=(w2, ymax), xytext=(w2, 0), ha='center', color='red')


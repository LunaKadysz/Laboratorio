# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 17:10:55 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



# C = 0.01microF
# R = 4000 Ohms
# frec = 300Hz
# Vpicopico = 5V con offset de 2.5V


data = np.loadtxt('RC.txt')
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


def chisqg(ydata,ymod,sd=None):  
      """  
 Returns the chi-square error statistic as the sum of squared errors between  
 Ydata(i) and Ymodel(i). If individual standard deviations (array sd) are supplied,   
 then the chi-square error statistic is computed as the sum of squared errors  
 divided by the standard deviations.     Inspired on the IDL procedure linfit.pro.  
 See http://en.wikipedia.org/wiki/Goodness_of_fit for reference.  
   
 x,y,sd assumed to be Numpy arrays. a,b scalars.  
 Returns the float chisq with the chi-square statistic.  
   
 Rodrigo Nemmen  
 http://goo.gl/8S1Oo  
      """  
      # Chi-square statistic (Bevington, eq. 6.9)  
      if sd==None:  
           chisq=np.sum((ydata-ymod)**2)  
      else:  
           chisq=np.sum( ((ydata-ymod)/sd)**2 )  
        
      return chisq  
chi = chisqg(V, f(t,param[0],param[1],param[2]))
print("chisquered: " + chi)



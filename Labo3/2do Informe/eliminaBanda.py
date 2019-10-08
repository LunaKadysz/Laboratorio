# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:44:06 2019

@author: Publico
"""

# T = 1/(np.sqrt((1-(frec*(sqrt(L*C)))**2)**2+((frec*(sqrt(L*C)))*(rl* np.sqrt(C/L)))**2)) 
#[frec] = Hz f0 = 225.07hz +- err
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
 
L = 0.5 #[Henrios]
C = 0.000001 #[Faradios]
R = 1000 #[Ohms]
w0 = 1/np.sqrt(L*C) #[Hz]
Q = (1/R)*np.sqrt(L/C)
print(w0)
print(Q)

#datos
frec = np.array([40,60,80,100,120,140,160,180,200,210,225,240,260,280,300,320,340,360,380,400])
V_ent = np.array([9.8,9.76,9.76,9.84,9.84,9.92,9.92,9.92,10,10,10,10,10,9.96,9.92,9.92,9.92,9.92,9.84,9.84])
V_sal = np.array([8.12,7.92,7.76,7.44,6.96,6.32,5.52,4.48,3.44,2.96,2.8,3.12,4.12,5.12,6,6.72,7.32,7.68,8.04,8.32])

#errores
err_Vent = np.array([0.005*len(frec)])
err_Vsal = np.array([0.005*len(frec)])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)


#esta funcion es la que esta mal. fittea cualquier cosa.
#def f(frec,f0):
 #   return ((2*np.pi*frec)**2 + (2*np.pi*f0)**2)/((2*np.pi*frec)**2 + (100*(2*np.pi*frec)) + (2*np.pi*f0)**2)      
def f(frec,f0,E,A0,T0):
    w = 2*np.pi*frec
    w0 = 2*np.pi*f0
    A = (w/w0)-(w0/w)
    B = 2*E
    C = (B/A)**2
    return (A0/np.sqrt(1+C))+T0

#tira = np.linspace(0,500,1)
#g = f(tira,225,0)
#
#plt.plot(tira,g,'--',color='green')
#plt.show()

 #fitteo con la funcion chota 
param, param_cov = curve_fit(f,frec, (V_sal/V_ent), p0=[225,0.1,0.6,0.3]) #p0 son los parametros de estimacion

#esto va a imprimir en la consola el parametro estimado
print("f0") 
print(param[0]) 
print("E")
print(param[1])
print("A0")
print(param[2])
print("T0")
print(param[3])

print("Covariance of coefficients:") 
print(param_cov) 
  

ans1 = f(frec,param[0],param[1],param[2],param[3]) #si agregan mas parametros van a tener que agregarlos aca con una coma y param[n]
 
#esto no lo toquen, porque ya esta configurado aunque cambien la funcion de arriba
plt.errorbar(frec,np.sqrt((V_sal/V_ent)**2),yerr=propagacion, fmt='.',color ='black',label ="Datos", ecolor = 'red')
plt.plot(frec, ans1, '--', color ='blue', label ="Ajuste") 
plt.title('Eliminabanda')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Transferencia ')
plt.legend()
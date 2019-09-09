# -*- coding: utf-8 -*-



                         ##### Kirchhoff #####
 ## Ley 1: Nodos
 # [I] = mA ; [R] = Ohm ; QUE ESCALA USAMOS??
 # en I1 están las distintas mediciones con el amperímetro del cable1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from scipy.optimize import curve_fit 
 
I0 = 3.4
I1 = np.array([1.7,2.6,2.8,3])
I2 = np.array([1.7,0.8,0.5,0.4])
R1 = np.array([1000,666,600,571])
R2 = np.array([1000,2000,3000,4000])
 
# y-axis in bold
rc('font', weight='bold')

r = np.array([0,1,2,3])
names = ['1','2','3','4']
barWidth = 1
 
plt.bar(r, I1, color='green', edgecolor='white', width=barWidth, label ="I1")
plt.bar(r, I2, bottom=I1, color='orange', edgecolor='white', width=barWidth, label ="I2")

plt.xticks(r, names, fontweight='bold')
plt.xlabel("Disposición N°")
plt.ylabel("Suma de las Corrientes [mA]")

  
def f(x,m,k): 
    return x*m+k
  
param, param_cov = curve_fit(f,r,I1+I2) 
  
print("Corriente sumada:") 
print(param[1]) 
print("Covariance of coefficients:") 
print(param_cov) 
e = np.linspace(-0.6,3.6, 20)
ans1 = (param[0] * e + param[1])
plt.plot(e, ans1, '--', color ='blue', label ="Ajuste Constante") 
plt.show()

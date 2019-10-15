# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:27:17 2019

@author: Publico
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

#R1 = 1000+- 50
#R2 = 1000 +- 50
# Rthevennin en el caso limite = 672.86
#R4 = 507

#Vcd = 10


def puente(R3,R4):
    Vcd = 10
    R1 = 1000
    R2 = 1000
    return Vcd*((R1*R4-R2*R3)/-((R1+R2)*(R3+R4)))


R3 = np.array([107,207,307,407,487,497,507,517,527,537,547,557,607,657,707,757,807,1007,1207,1407,1607,1807,2007,2507,3007,3507,4507,5507,6507,8007,10007])
err_R3 = np.array([0.0005])

Vab = np.array([-3.23,-2.08,-1.222,-0.545,-0.1025,-0.0515,0,0.048,0.0956,0.141,0.187,0.232,0.445,0.640,0.818,0.982,1.134,1.643,2.03,2.34,2.59,2.79,2.97,3.3,3.54,3.72,3.97,4.13,4.2,4.38,4.49])
err_Vab = np.array([0.001,0.001,0.001,0.001,0.0005,0.001,0.005,0.001,0.001,0.001,0.001,0.001,0.001,0.002,0.001,0.001,0.001,0.001,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01])

param, param_cov = curve_fit(puente,R3,Vab, p0=[507]) 
plt.plot(R3,puente(R3,param[0]), '--', color ='red', label ="Ajuste") 
plt.scatter(R3,Vab, label ="Datos")

R4 = param[0]


def sens(R3,R4):
    return R3*R4/(R3+R4)**2


plt.figure()
plt.scatter(R3,sens(R3,R4))
plt.legend()
plt.show()
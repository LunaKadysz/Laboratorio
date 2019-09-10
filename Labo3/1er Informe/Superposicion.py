# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 19:04:05 2019

@author: Publico
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from scipy.optimize import curve_fit 
# [V] = v , [R] = Ohm

R1 = 3000
R2 = 6000
R3 = 1000

V1 = np.array([5, 7, 9])
V2 = np.array([7, 7, 7])

I12 =np.array([1.832, 2.33, 2.77])
err_I12 = np.array([0.001, 0.005, 0.005])

I2 = np.array([0.754,0.754,0.754])
I1 = np.array([1.08,1.508,1.935])

# y-axis in bold
rc('font', weight='bold')
barWidth = 0.33
r1 = np.array([0,1,2])
r2 = [x + barWidth for x in r1]
names = ['1','2','3']

 
plt.bar(r1, I1, color='green', edgecolor='white', width=barWidth, label ='I1')
plt.bar(r1, I2, bottom=I1, color='orange', edgecolor='white', width=barWidth, label ='I2')
plt.bar(r2, I12, color='purple', width=barWidth, edgecolor='white', label ='I')

plt.xticks(r1, names, fontweight='bold')
plt.xlabel("Disposición N°")
plt.ylabel("Suma de las Corrientes [mA]")
plt.ylim(0,4)
plt.title("superposicion")
plt.legend(loc='best') 
plt.show()

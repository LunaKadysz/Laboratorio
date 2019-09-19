# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:46:04 2019

@author: Luna Kadysz
"""

 # [tiempo]= ms
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


waiting_viejo = [25.43,32.27,17.02,48.97,29.12]
threading = [18.91,15.23,14.29,14.53,14.99]
ry = waiting_viejo + threading

rc('font', weight='bold')
barWidth = 0.33
r1 = [0,1,2,3,4]
r2 = ([x + barWidth for x in r1])
r = r1 + r2
names = ['155','154','90','76','26']

 
plt.bar(r1, waiting_viejo, color='green', edgecolor='white', width=barWidth, label ='Promedio viejo: ' + str(round(np.average(waiting_viejo), 2)) + 's')
plt.bar(r2, threading, color='orange', width=barWidth, edgecolor='white', label ='Promedio multithreading: '+ str(round(np.average(threading), 2)) + 's')

for i in range(len(r)):
    plt.text(x = r[i]-0.1 , y = ry[i]+0.1, s = ry[i], size = 6)


plt.xticks(r1, names, fontweight='bold')
plt.xlabel("Nuemero de Solicitud")
plt.ylabel("Tiempo [s]")
plt.title("")
plt.legend(loc = 'upper left') 
plt.show()
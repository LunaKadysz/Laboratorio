# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:46:04 2019

@author: Luna Kadysz
"""

 # [tiempo]= ms
 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc


waiting_viejo = np.array([25.43,32.27,17.02,48.97,29.12])
waiting_nuevo = np.array([])


rc('font', weight='bold')
barWidth = 0.33
r1 = np.linspace(0,len(waiting_viejo)-1,len(waiting_viejo))
r2 = [x + barWidth for x in r1]
names = ['155','154','90','76','26']

 
plt.bar(r1, waiting_viejo, color='green', edgecolor='white', width=barWidth, label ='Promedio viejo: ' + str(round(np.average(waiting_viejo), 2)) + 'ms')
#plt.bar(r2, I12, color='purple', width=barWidth, edgecolor='white', label ='I')

plt.xticks(r1, names, fontweight='bold')
plt.xlabel("Nuemero de Solicitud")
plt.ylabel("Tiempo [ms]")
plt.title("")
plt.legend(loc='best') 
plt.show()
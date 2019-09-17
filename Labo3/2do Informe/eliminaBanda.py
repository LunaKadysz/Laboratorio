# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:44:06 2019

@author: Publico
"""

#[frec] = Hz f0 = 225.07hz +- err
import numpy as np
import matplotlib.pyplot as plt
 
frec = np.array([40,60,80,100,120,140,160,180,200,210,225,240,260,280,300,320,340,360,380,400])
V_ent = np.array([9.8,9.76,9.76,9.84,9.84,9.92,9.92,9.92,10,10,10,10,10,9.96,9.92,9.92,9.92,9.92,9.84,9.84])
V_sal = np.array([8.12,7.92,7.76,7.44,6.96,6.32,5.52,4.48,3.44,2.96,2.8,3.12,4.12,5.12,6,6.72,7.32,7.68,8.04,8.32])



err_Vent = np.array([0.005*len(frec)])
err_Vsal = np.array([0.005*len(frec)])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)


plt.errorbar(frec,V_sal/V_ent,yerr=propagacion, fmt='o',color ='black',label ="Datos", ecolor = 'red')
plt.show()
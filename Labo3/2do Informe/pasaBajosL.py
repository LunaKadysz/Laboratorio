# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:54:47 2019

@author: Publico
"""

#[frec] = Hz f0 = 320hz +- err
import numpy as np
import matplotlib.pyplot as plt
 
frec = np.array([10,50,100,160,200,220,240,260,280,300,320,340,360,380,400,420,450,500,550,600,700,800,900,1000,1250])
V_ent = np.array(len(frec)*[9.92])
V_sal = np.array([8.24,8.16,7.96,7.68,7.44,7.29,7.12,6.96,6.8,6.64,6.44,6.28,6.16,6,5.84,5.68,5.48,5.16,4.88,4.64,4.08,3.72,3.44,3.12,2.56])



err_Vent = np.array([0.005*len(frec)])
err_Vsal = np.array([0.005*len(frec)])
propagacion = np.sqrt((err_Vsal/V_ent)**2+(V_sal*err_Vent/(V_ent)**2)**2)


plt.errorbar(frec,V_sal/V_ent,yerr=propagacion, fmt='o',color ='black',label ="Datos", ecolor = 'red')
plt.show()
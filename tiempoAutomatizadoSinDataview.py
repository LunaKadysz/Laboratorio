# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 12:14:26 2019

@author: Luna Kadysz
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gaussian_kde


ti = np.loadtxt('tiempoInicial.txt')
tf = np.loadtxt('tiempoFinal.txt')
tiempo = (tf - ti) / 1000
density = stats.kde.gaussian_kde(tiempo)
x = np.arange(0., 4, .01)

plt.xlabel("Tiempo [s]")
plt.ylabel("Cantidad")
plt.title("Tiempo en cargar sin Dataview")
plt.ylim(0,1.20)
plt.plot(x,density(x), color="b",label = 'Mediana: ' + str(round(np.mean(tiempo), 2)))
plt.vlines(np.mean(tiempo), 0, density(np.mean(tiempo)), linestyles= '--', color ='red')
plt.annotate(round(np.mean(tiempo), 2), xy=(np.mean(tiempo), density(np.mean(tiempo))), xytext=(np.mean(tiempo)+0.15, density(np.mean(tiempo))), ha='center', color='red')
plt.legend()
plt.show()


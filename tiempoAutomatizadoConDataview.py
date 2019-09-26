# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:00:38 2019

@author: Luna Kadysz
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import gaussian_kde


ti = np.loadtxt('tiempoInicial2.txt')
tf = np.loadtxt('tiempoFinal2.txt')
tiempo = (tf - ti) / 1000
time = np.delete(tiempo,np.arange(0,29,1))
density = stats.kde.gaussian_kde(time)
x = np.arange(-10, 40, .1)

plt.xlabel("Tiempo [s]")
plt.ylabel("Cantidad")
plt.title("Tiempo en cargar con Dataview")
plt.ylim(0,0.06)
plt.plot(x,density(x), color="b",label = 'Mediana: ' + str((round(np.mean(time), 2))))
plt.vlines(np.mean(time), 0, density(np.mean(time)), linestyles= '--', color ='red')
plt.annotate(round(np.mean(time), 2), xy=(np.mean(time), density(np.mean(time))), xytext=(np.mean(time)+0.65, density(np.mean(time))), ha='center', color='red')
plt.legend()
plt.show()


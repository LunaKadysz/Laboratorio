# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:23:44 2019

@author: Luna
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Definimos la función
f = lambda x, A,T,C: A*np.exp(-x/T)+C

# Definimos los parámetros
A = 1
T = 10
C = 5

# Definimos dominio e imagen
x = np.linspace(-20, 20, 100)
y = f(x,A,T,C)

# Creamos un ruido y lo agregamos a los datos
ruido =  (2*(np.random.random(len(y)))-1)*0.2*y
y_data = y + ruido
# Proponemos un error
error_y = 0.1*y
#error_x = 0.05*x

np.savetxt('Datos_taller.txt', [x,y_data, error_y], delimiter = '\t')
Data = np.loadtxt('Datos_taller.txt', delimiter = '\t')

plt.plot(Data[0],Data[1], 'r.') # Veamos que son los mismos datos
plt.errorbar(Data[0], Data[1], Data[2], linestyle = 'None')
plt.show()

popt, pcov = curve_fit(f, x, y_data, sigma = error_y)
sigmas = [pcov[0,0],pcov[1,1], pcov[2,2]]
print(popt, sigmas)

plt.plot(x, y, 'b-', label = 'Modelo')
plt.plot(x,y_data, 'r.', label = 'Datos')
plt.plot(x,f(x, popt[0], popt[1],popt[2]), 'g-', label = 'Ajuste') # Hacemos el gráfico en otro color de
                                                                   #la función evaluada en los parámetros ajustados
plt.errorbar(x, y_data, error_y, linestyle = 'None')

# Detalles del gráfico
plt.grid(True)
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best')

plt.show()






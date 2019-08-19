# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:06:19 2019

@author: Luna
"""

#Hagan un ajuste sobre la función $f(x) = Acos(\omega x)$ con $A = 2$ y $\omega = 3$ 
#para 40 valores en $Dom = [-\pi, \pi]$ con valores que varían el 15% del valor dado 
#por el modelo, y compare los parámetros obtenidos con los dados.
#Bonus track: Se puede escribir en LaTeX sobre los gráficos. 
#Averiguen qué biblioteca hace falta importar y presenten los parámetros 
#ajustados en el título.
import pylab
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

f = lambda x, A,o: A*np.cos(o*x)
A=2
o=3
x = np.linspace(-np.pi, np.pi , 80)
y = f(x,A,o)

# Creamos un ruido y lo agregamos a los datos
ruido =  (2*(np.random.random(len(y)))-1)*0.2*y
y_data = y + ruido
# Proponemos un error
error_y = 0.1*y

np.savetxt('Datos_coseno.txt', [x,y_data, error_y], delimiter = '\t')
data = np.loadtxt('Datos_coseno.txt', delimiter = '\t' )

plt.plot(data[0],data[1], 'r.') # Veamos que son los mismos datos
plt.errorbar(data[0], data[1], data[2], linestyle = 'None')
plt.show()

popt , pcov = curve_fit(f, x, y_data, sigma = error_y)
sigmas = [pcov[0,0],pcov[1,1]]
print(popt)

pylab.plot(x, y, 'b-', label = 'Modelo')
plt.plot(x, f(x, popt[0], popt[1]), 'g-', label = 'Ajuste') # Hacemos el gráfico en otro color de
                                                                #la función evaluada en los parámetros ajustados
plt.errorbar(x, y_data, error_y, linestyle = 'None')

# Detalles del gráfico
plt.grid(True)
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best')

plt.show()









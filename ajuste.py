from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
data = np.loadtxt("doble_exp.dat") 

x = data[:,0]
y = data[:,1]
yerrado = data[:,2]
error_y = data[:,3]



# Detalles del gráfico
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best') 
plt.yscale('log')
plt.xscale('log')
plt.errorbar(x, yerrado, yerr=error_y, fmt='go', label="Datos", ecolor = 'red')
plt.show() 


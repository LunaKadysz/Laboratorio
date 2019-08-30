from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
data = np.loadtxt("doble_exp.dat") 

x = data[:,0]
y = data[:,1]
yerrado = data[:,2]
error_y = data[:,3]

f = lambda x, A, B: A * np.exp(B*x) 

A0 = 40
B0 = -3


init_guess = [A0, B0]

popt, pcov = curve_fit(f, x, yerrado, p0=init_guess)    

# guardamos los resultados que nos interesan del ajuste, los parámetros A y k

A_fit = popt[0]
B_fit = popt[1]

# generamos la curva que vamos a graficar (¡Ojo, el ajuste devolvió dos parámetros no una curva!)

ajuste = f(x, A_fit, B_fit)
plt.plot(x, ajuste, 'b', linewidth=2.0)
plt.plot(x,y)
# Detalles del gráfico
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best') 

plt.errorbar(x, yerrado, yerr=error_y, fmt='go', label="Datos", ecolor = 'red')
plt.show() 
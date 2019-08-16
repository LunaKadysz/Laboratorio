from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
data = np.loadtxt("doble_exp.dat") 

x = data[:,0]
y = data[:,1]
yerrado = data[:,2]
error_y = data[:,3]


f = lambda x, A, B: A * x + B

# Ajustamos, pero con las funciónes logaritmicas. Usamos propagación de errores
popt, pcov = curve_fit(f, np.log(x), np.log(y), sigma = 1/y * error_y, 
                       absolute_sigma=True)

print(popt)
print(pcov)



# Detalles del gráfico
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best') 
plt.yscale('sqrt')
plt.xscale('sqrt')
plt.errorbar(x, yerrado, yerr=error_y, fmt='go', label="Datos")
plt.show() 


import numpy as np
import matplotlib.pyplot as plt


 # ese array tiene 1000 elementos, andar printeando es poco práctico!
x = np.linspace(0, 5, 40)
y = x**2
plt.plot(x, y, 'ro')
plt.axis([0, 6, -20, 26])

def f(t):
    return 40 * np.exp(-t) * np.cos(8*np.pi*t)
plt.plot(x, f(x), 'b')

plt.show()

sigma = 0.8 
ruido=[]
ruidoo=[]
# creating a noise with the same dimension as the dataset (2,2) 
for i in np.nditer(y):
    mu = i
    ruido1 = np.random.normal(mu, sigma,1) 
    ruido2 = np.random.exponential(1.0,1)
    ruido.append(ruido1)
    ruidoo.append(ruido2)
#np.savetxt('doble_exp.dat', (x,y),delimiter="\n", newline='\r\n')
print(ruido,ruidoo)

np.savetxt('doble_exp.dat',np.transpose([x,y,ruido,ruidoo]))   
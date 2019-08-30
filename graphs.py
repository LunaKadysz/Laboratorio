import numpy as np
import matplotlib.pyplot as plt


 # ese array tiene 1000 elementos, andar printeando es poco práctico!
x = np.linspace(0, 5, 40)
y = x**2
plt.plot(x, y, 'ro')
plt.axis([0, 6, -20, 26])

def f(t):
    return 40* np.exp(-3*t)
plt.plot(x, f(x), 'b')

plt.show()

sigma = 2 
ruido=[]
ruidoo=[]
# creating a noise with the same dimension as the dataset (2,2) 
for i in np.nditer(f(x)):
    mu = i
    ruido1 = np.random.normal(mu, sigma,1) 
    ruido2 = np.random.normal(0,4,1)
    ruido.append(ruido1)
    ruidoo.append(ruido2)
#np.savetxt('doble_exp.dat', (x,y),delimiter="\n", newline='\r\n')
print(ruidoo)

np.savetxt('doble_exp.dat',np.transpose([x,f(x),ruido,ruidoo]))   
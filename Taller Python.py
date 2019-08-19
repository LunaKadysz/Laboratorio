# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 17:20:27 2019

@author: Luna
"""

import numpy as np
from numpy import linalg

# equiespaciados
equilin = np.linspace(0, 1, 9) # 10 número equiespaciados linealmente entre 0 y 1
print('Equiespaciado lineal:', equilin)

arange = np.arange(0, 1, 1./10) # como el range de Python pero puede venir con un paso en coma flotante
print('Como el range de las listas:', arange)

identidad = np.identity(3)
print('Identidad de 3x3:', identidad)
print()

ojos = np.eye(5, k=0) # unos en la diagonal, como identidad
print('Identidad 5x5', ojos)

ojos2 = np.eye(5, k=2) # qué pasó acá?
print(ojos2)

x = np.linspace(0, 10, 1000) # ese array tiene 1000 elementos, andar printeando es poco práctico!
print(x.dtype) # array.dtype nos dice que tipo de elementos tiene el array


A = np.arange(1,17).reshape(4,4)
print(A)

v = np.array([1, 1, 1])
w = np.array([2, 2, 2])
z = np.array([1, 0, 1])

norma =linalg.norm(v) # la norma 2 / módulo del vector v
print(norma)
print(np.sqrt(3)) # calculado a mano
print(norma == np.sqrt(3)) # y numpy sabe que son lo mismo

m = [0,1,0,1]
print(m)







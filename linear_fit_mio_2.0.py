# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 21:06:11 2019

@author: Luna
"""

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab
from scipy.optimize import curve_fit

# Scientific libraries
import numpy
from numpy import arange,array
from scipy import stats

xe = arange(0,8)
ye = [10, 15, 22 , 26 , 29 , 35 , 41, 47]

i=0
sum=0 
def pendiente(ye,i,sum):
    for i in range(7):
        sum = sum + (ye[i+1]-ye[i])
    ym=sum/7    
    return ym

m = pendiente(ye,i,sum)
print(m)
b = 10
y= m*xe+b

plt.figure('Funcion')
plt.xlabel('Distancia (cm)')
plt.ylabel('Amplitud (V)')   
plt.scatter(xe,ye)
plt.plot(xe,y, 'r')
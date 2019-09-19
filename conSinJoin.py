# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:53:47 2019

@author: Luna Kadysz
"""
import numpy as np
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

sin_join = np.array([3.17,2.67,2.88,5.74,2.76,2.68,2.65,3.45,2.77,2.89,2.81,2.94,3.19,3.19,2.94,2.89,6.3,3.78,4.63,4.48,3.98,3.99])
con_join = np.array([2.54,2.44,2.59,2.44,2.75,2.51,2.48,3.26,3.07,2.48,4.75,2.49,2.64,2.69,2.81,2.6,2.7,2.53,3.14,2.7,2.93,2.75])


sin = stats.mode(sin_join)
con = stats.mode(con_join)



p1=sns.kdeplot(sin_join, shade=True, bw=.05, color="r",label = 'Sin join moda: ' + str(sin[0]) )
p1=sns.kdeplot(con_join, shade=True, bw=.05, color="b",label = 'Con join moda: ' + str(con[0]))
#plt.xticks(np.linspace(2,7,10), np.linspace(2,7,10), fontweight='bold')
plt.xlabel("Colors")
plt.ylabel("Values")
plt.title("Colors vs Values") # You can comment this line out if you don't need title
plt.show(p1)
plt.hist(sin_join, bins=10)
sns.plt.show()

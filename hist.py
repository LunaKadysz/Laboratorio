# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 08:53:47 2019

@author: Luna Kadysz
"""

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.random_integers(2000, 2019, 80)
x2 = np.random.random_integers(2000, 2019, 100)
score_india = x1
legend = ['Mujeres', 'Hombres']
score_pk = x2
plt.hist([score_india, score_pk], color=['purple', 'green'])
plt.xlabel("Sueldo mensual por año")
plt.ylabel("De a miles (Pesos)")
plt.legend(legend)
plt.xticks(range(2000, 2019,2))
plt.yticks(range(1, 17))
plt.title('Champions Trophy 2017 Final\n Runs scored in 3 overs')
plt.show()

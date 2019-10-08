#ANTIRESONANCIA

import numpy as np
import matplotlib.pyplot as plt

R_lim = 1000

V1 = np.array([38.2,37.6,35.0,29.2,26.8,24.0,20.8,18.0,15.0,14.2,12.6,12.4,11.8,13.4,14.8,18.0,20.6,27.4,32.6,36.4,38.8,42.8,44.6,46.6])
err_V1 = np.array([0.2,0.2,0.2,0.2,0.1,0.4,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])

frec1 = np.array([20.0,29.97,60.09,89.9,100.2,110.0,120.0,130.0,140.0,144.9,150.0,155.2,160.0,170.0,180.1,190.0,200.2,225.0,250.3,275.0,300.0,350.0,400.0,500.0])
err_frec1 = np.array([0.05,0.2,0.2,0.2,0.2,0.2,0.2,0.5,0.4,0.3,0.4,0.4,0.5,0.4,0.3,0.3,0.2,0.3,0.3,0.3,0.5,0.5,0.5,1])


V2 = np.array([16.4,18.0,22.0,27.6,32.8,36.8,40.4,42.8,44.4,45.4,46.2])
err_V2 = np.array([0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2])

frec2 = np.array([20.0,50.0,100.0,150.0,200.2,250.0,300.0,350.0,400.0,450.0,500.0])
err_frec2 = np.array([0.08,0.1,0.2,0.2,0.4,0.4,0.4,0.4,0.3,0.4,0.8])


plt.figure()
plt.scatter(frec1, V1/R_lim)
plt.scatter(frec2, V2/R_lim, color = "orange")
plt.show()
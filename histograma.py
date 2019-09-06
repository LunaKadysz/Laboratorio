# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 08:51:54 2019

@author: Luna Kadysz
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
# example data
mu = 100 # mean of distribution
sigma = 15 # standard deviation of distribution
x = mu + sigma * np.random.randn(10000)

num_bins = 20

# N is the count in each bin, bins is the lower-limit of the bin
N, bins, patches = plt.hist(x, bins=num_bins)
y = mlab.normpdf(bins, mu, sigma)
# We'll color code by height, but you could use any scalar
fracs = N / N.max()

# we need to normalize the data to 0..1 for the full range of the colormap
norm = colors.Normalize(fracs.min(), fracs.max())

# Now, we'll loop through our objects and set the color of each accordingly
for thisfrac, thispatch in zip(fracs, patches):
    color = plt.cm.viridis(norm(thisfrac))
    thispatch.set_facecolor(color)


# We can also normalize our inputs by the total number of counts
plt.hist(x, bins=num_bins, density=True, color = np.array(thispatch))

# Now we format the y-axis to display percentage
plt.yaxis.set_major_formatter(PercentFormatter(xmax=1))
plt.show()
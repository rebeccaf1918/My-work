# Weekly Task 08
# plottask.py
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Rebecca Feeley

import numpy as np 
from numpy import random
import matplotlib.pyplot as plt

np.random.seed(1)
histogram = np.random.normal(loc=5, scale = 2, size = 1000)

plt.hist(histogram)
#plt.show()

xpoints = np.array(range(1,11))
ypoints = pow(xpoints, 3)

plt.plot (xpoints, ypoints)
plt.show()

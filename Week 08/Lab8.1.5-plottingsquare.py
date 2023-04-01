# plottingsquare.py
# Program that plots the function y = x squared
# Author: Rebecca Feeley

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself to square it

plt.plot(xpoints, ypoints)
plt.show()

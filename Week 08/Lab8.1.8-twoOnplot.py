# twoOnplot.py
# Program that shows two previous plots on the same plot
# Author: Rebecca Feeley

import numpy as np
import matplotlib.pyplot as plt

min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) # this is so the 'random' numbers are the same each time so its easier to debug
salaries = np.random.randint(min_salary, max_salary, number_of_entries)

ages = np.random.randint(low = 21, high = 66, size = number_of_entries)

plt.scatter(ages, salaries)
#plt.show() #if this is included here, the program will stop here until plot is closed

# add x squared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply each entry by itself to get the squared 

plt.plot(xpoints, ypoints, color = 'r')
plt.show() 

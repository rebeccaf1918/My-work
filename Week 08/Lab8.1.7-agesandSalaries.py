# agesandSalaries.py
# Program that makes a scatter plot of the salaries and ages from previous labs
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
plt.show()

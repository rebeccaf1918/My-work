# makelistseed.py
# Program that makes the random salaries chosen the same each time
# Author: Rebecca Feeley

import numpy as np
min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) # this is so the 'random' numbers are the same each time so its easier to debug
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print (salaries)


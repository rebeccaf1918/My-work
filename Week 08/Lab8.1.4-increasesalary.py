# increasesalary.py
# Program that increases all salaries by 5%
# Author: Rebecca Feeley

import numpy as np
min_salary = 20000
max_salary = 80000
number_of_entries = 10

np.random.seed(1) # this is so the 'random' numbers are the same each time so its easier to debug
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print (salaries)

# add 5000 to each value
salaries_plus = salaries + 5000
print (salaries_plus)

salaries_multiply = salaries * 1.05 # add 5% by multiplying value by 1.05
print (salaries_multiply)

# this is a float array to convert to an int array (it does a floor)
new_salaries = salaries_multiply.astype(int)
print (new_salaries)

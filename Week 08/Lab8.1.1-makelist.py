# makelist.py
# Program that makes a list of salaries from 20,000 to 80,000 with 10 random numbers chosen
# Author: Rebecca Feeley

import numpy as np
min_salary = 20000
max_salary = 80000
number_of_entries = 10

salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print (salaries)



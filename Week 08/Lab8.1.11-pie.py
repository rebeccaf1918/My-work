# pie.py
# Program making a pit plot of the unique occurances of values in an array
# Author: Rebecca Feeley

import numpy as np 
import matplotlib.pyplot as plt

# make the array of occurances
possible_counties = ["Mayo", "Sligo", "Wexford", "Cork", "Roscommon"]

# pick 100 randomly from possible counties with the frequence set in p
counties = np.random.choice(possible_counties, p=[0.1, 0.3, 0.2, 0.12, 0.28 ], size = (100))

# to get the number of occurances of each county
# this gives a tuple of the unique values and how often they appear
unique, counts = np.unique(counties, return_counts=True)
plt.pie(counts, labels = unique)

plt.show()
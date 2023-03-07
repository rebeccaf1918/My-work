# topThree.py
# generates 10 random numbers (0-100),
# prints them out then prints out the top three
# Author: Rebecca Feeley

import random

howMany    = 10
topHowMany = 3
rangeFrom  = 0
rangeto    = 100

numbers = []

for i in range(0,howMany):
    numbers.append(random.randint(rangeFrom,rangeto))
print (f"{howMany} random numbers\t {numbers}")
# I am keeping the original list
topOnes = numbers.copy()
topOnes.sort(reverse = True)
print ("The top {topHowMany} are \t\t {topOnes[0:topHowMany]}")

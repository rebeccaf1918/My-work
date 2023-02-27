# randomFruit2.py
# This program prints out a random fruit
# using a tuple 

# Author: Rebecca Feeley

import random

fruits = ("Apple", "Orange", "Pear", "Banana")
# A random number between 0 and length-1 is required

index = random.randint(0,len(fruits)-1)

fruit = fruits[index]

print ("A Random Fruit: {}".format(fruit))


# randomGenerator.py
#  program that prints out a random number between 1 and 10

# program that prompts user to input two numbers and prints out a random number in that range
# Author: Rebecca Feeley

import random

number =  random.randint(1,10)

print("Here is a random number {}".format(number))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

number = random.randint(x, y)

print("Here is a random number {}".format(number))



